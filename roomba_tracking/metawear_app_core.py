import sys
import os
from PyQt5.QtWidgets import QDialog, QApplication
from metawear_gui import *
from mbientlab.metawear import MetaWear, libmetawear, parse_value, create_voidp, create_voidp_int
from mbientlab.metawear.cbindings import *
import time
from threading import Event
from pandas import DataFrame
import logging
from datetime import datetime

__datefmt__ = '%Y%m%d %I:%M:%S'
__now__ = str(int(time.time()))

logging.basicConfig(filename='logs/{0}_metawear.log'.format(__now__), filemode='w', level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s', datefmt=__datefmt__)

class MyForm(QDialog):
    def __init__(self):

        super().__init__()
        self.ui = Ui_MetawearApp()
        self.ui.setupUi(self)
        self.ui.buttonConnect.clicked.connect(self.buttonConnnect)
        self.ui.buttonGatherData.clicked.connect(self.buttonGatherData)
        self.ui.buttonExit.clicked.connect(self.exiting)
        self.ui.buttonDownloadData.clicked.connect(self.buttonDownloadData)
        self.show()

    def buttonConnnect(self):
        self.ui.labelConnect.setText('Connecting...')
        self.ui.labelConnect.repaint()

        if s.connect_to_sensor() == 1:
            self.ui.labelConnect.setText('Connected!')
        else:
            self.ui.labelConnect.setText('Failed')

    def buttonGatherData(self):
        seconds = self.ui.secondsSpin.value()
        self.ui.labelGatherData.setText('Gathering...')
        self.ui.labelConnect.repaint()

        if s.gather_data(seconds) == 1:
            self.ui.labelGatherData.setText('Complete!')
        else:
            self.ui.labelGatherData.setText('Failed')

    def buttonDownloadData(self):
        name = self.ui.nameText.text()
        self.ui.labelDownloadData.setText('Downloading...')
        self.ui.labelDownloadData.repaint()

        if s.download_data(name) == 1:
            self.ui.labelDownloadData.setText('Data saved.')
        else:
            self.ui.labelDownloadData.setText('Failed')

    def exiting(self):
        s.reset_device
        exit()

class Sensor():
    def __init__(self):
        
        self.device = MetaWear('C7:CF:3D:0E:D9:0E')
        self.default_name = '_temp_data.txt'

    def connect_to_sensor(self):
        self.device.connect()
        self.signal = libmetawear.mbl_mw_acc_get_acceleration_data_signal(self.device.board)
        self.logger = create_voidp(lambda fn: libmetawear.mbl_mw_datasignal_log(self.signal, None, fn), resource = "acc_logger")
        logging.info('metawear device connected')
        return 1

    def gather_data(self, seconds=3):
        try:
            libmetawear.mbl_mw_logging_start(self.device.board, 0)
            libmetawear.mbl_mw_acc_enable_acceleration_sampling(self.device.board)
            libmetawear.mbl_mw_acc_start(self.device.board)
            logging.info('data gathering started')

            time.sleep(seconds)

            libmetawear.mbl_mw_acc_stop(self.device.board)
            libmetawear.mbl_mw_acc_disable_acceleration_sampling(self.device.board)
            libmetawear.mbl_mw_logging_stop(self.device.board)
            logging.info('data gathering stopped')

        except RuntimeError as err:
            print(err)
            logging.info('runtime error in gather_data() occurred')
            return 0

        return 1

    def download_data(self, name='blank'):
        try:
            libmetawear.mbl_mw_settings_set_connection_parameters(self.device.board, 7.5, 7.5, 0, 6000)
            time.sleep(1.0)

            e = Event()
            def progress_update_handler(context, entries_left, total_entries):
                if (entries_left == 0):
                    e.set()
            
            fn_wrapper = FnVoid_VoidP_UInt_UInt(progress_update_handler)
            download_handler = LogDownloadHandler(context = None, \
                received_progress_update = fn_wrapper, \
                received_unknown_entry = cast(None, FnVoid_VoidP_UByte_Long_UByteP_UByte), \
                received_unhandled_entry = cast(None, FnVoid_VoidP_DataP))

            # print('Opening log file to write')
            f = open(name + self.default_name, 'a')

            callback = FnVoid_VoidP_DataP(lambda ctx, p: print("{epoch: %d, value: %s}" % (p.contents.epoch, parse_value(p)), file=f))
            libmetawear.mbl_mw_logger_subscribe(self.logger, None, callback)
            libmetawear.mbl_mw_logging_download(self.device.board, 0, byref(download_handler))
            e.wait()

            # close the file, process the data into a csv, then delete the original file
            f.close()
            self.process_data(name)
            os.remove(name + self.default_name)
            logging.info('data downloaded')

            return 1

        except RuntimeError as err:
            print(err)
            logging.info('runtime error in download_data() occurred')
            return 0

    def process_data(self, name):
        rows = {}
        for i in open(name + self.default_name, 'r'):
            epoch = i[8:21] 
            xyz = i[35:-3]
            xyz = xyz.replace(' ', '')
            xyz = xyz.replace(':', '')
            xyz = xyz.replace(',', '')
            xyz = xyz.replace('y', ' ')
            xyz = xyz.replace('z', ' ')
            x,y,z = xyz.split()
            
            rows[epoch] =  [x, y, z]

        df = DataFrame(rows.values(), index=rows.keys(), columns=['X', 'Y', 'Z'])
        df.to_csv('/home/nate/Projects/machine-learning/roomba_tracking/data/{0}_{1}_data.csv'.format(__now__, name))

    def reset_device(self):
        libmetawear.mbl_mw_debug_reset(self.device.board)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    s = Sensor()
    w = MyForm()
    w.show()
    sys.exit(app.exec_())