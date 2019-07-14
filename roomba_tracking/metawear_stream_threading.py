# usage: sudo python3 metawear_stream_example.py 'C7:CF:3D:0E:D9:0E'
# configured to run for 3 seconds

from __future__ import print_function
from mbientlab.metawear import MetaWear, libmetawear, parse_value
from mbientlab.metawear.cbindings import *
from time import sleep
from threading import Event

import platform
import sys
import threading
import pandas as pd

# if sys.version_info[0] == 2:
#     range = xrange

class State:
    def __init__(self, device):
        self.device = device
        self.samples = 0
        self.callback = FnVoid_VoidP_DataP(self.data_handler)
        self.df = pd.DataFrame(columns=['x', 'y', 'z'])

    def data_handler(self, ctx, data):
        parsed_data = str(parse_value(data))
        row_dict = {
            'x': parsed_data[5:10],
            'y': parsed_data[16:21],
            'z': parsed_data[27:32]
        }
        self.df = self.df.append(row_dict, ignore_index=True)
        
        # {x : 0.023, y : 0.030, z : 1.014}

        self.samples+= 1


class MetawearThread(threading.Thread):
    def __init__(self, duration):device_state
        threading.Thread.__init__(self)
        self.duration = duration
        self.mac = 'C7:CF:3D:0E:D9:0E'
        self.device_state = None
        print("Metawear thread initialized")

    def run(self):
        print("Starting...")

        # initialization
        d = MetaWear(self.mac)
        d.connect()
        print("Connected to " + d.address)
        self.device_state = State(d)

        print("Configuring device")
        libmetawear.mbl_mw_settings_set_connection_parameters(self.device_state.device.board, 7.5, 7.5, 0, 6000)
        sleep(1.5)

        libmetawear.mbl_mw_acc_set_odr(self.device_state.device.board, 100.0)
        libmetawear.mbl_mw_acc_set_range(self.device_state.device.board, 16.0)
        libmetawear.mbl_mw_acc_write_acceleration_config(self.device_state.device.board)

        signal = libmetawear.mbl_mw_acc_get_acceleration_data_signal(self.device_state.device.board)
        libmetawear.mbl_mw_datasignal_subscribe(signal, None, self.device_state.callback)

        libmetawear.mbl_mw_acc_enable_acceleration_sampling(self.device_state.device.board)
        libmetawear.mbl_mw_acc_start(self.device_state.device.board)

        print("Data gathering started")
        sleep(self.duration)

        # stop gathering
        libmetawear.mbl_mw_acc_stop(self.device_state.device.board)
        libmetawear.mbl_mw_acc_disable_acceleration_sampling(self.device_state.device.board)

        signal = libmetawear.mbl_mw_acc_get_acceleration_data_signal(self.device_state.device.board)
        libmetawear.mbl_mw_datasignal_unsubscribe(signal)
        libmetawear.mbl_mw_debug_disconnect(self.device_state.device.board)

        print("Total Samples Received")
        print("%s -> %d" % (self.device_state.device.address, self.device_state.samples))

# duration = 10
# threads = []

# thread1 = MetawearThread(duration)

# thread1.start()

# threads.append(thread1)

# seconds = 0

# dataframes = {}

# sleep(6)

# while seconds <= duration:
#     sleep(2)
#     dataframes[seconds] = thread1.states[0].df
#     thread1.states[0].df = pd.DataFrame(columns=['x', 'y', 'z'])
#     print(f'dataframe {seconds} created')
#     print(f'len {len(dataframes[seconds])}')
#     seconds += 2
    
# for t in threads:
#     t.join()

# print('Exiting main thread')