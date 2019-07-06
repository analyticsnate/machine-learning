# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metawear_2.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure


class Ui_MetawearApp(object):
    def setupUi(self, MetawearApp):
        MetawearApp.setObjectName("MetawearApp")
        MetawearApp.resize(986, 402)
        self.buttonConnect = QtWidgets.QPushButton(MetawearApp)
        self.buttonConnect.setGeometry(QtCore.QRect(30, 110, 121, 31))
        self.buttonConnect.setObjectName("buttonConnect")
        self.labelConnect = QtWidgets.QLabel(MetawearApp)
        self.labelConnect.setGeometry(QtCore.QRect(160, 120, 181, 17))
        self.labelConnect.setObjectName("labelConnect")
        self.buttonGatherData = QtWidgets.QPushButton(MetawearApp)
        self.buttonGatherData.setGeometry(QtCore.QRect(30, 150, 121, 31))
        self.buttonGatherData.setObjectName("buttonGatherData")
        self.labelGatherData = QtWidgets.QLabel(MetawearApp)
        self.labelGatherData.setGeometry(QtCore.QRect(160, 160, 171, 17))
        self.labelGatherData.setObjectName("labelGatherData")
        self.buttonExit = QtWidgets.QPushButton(MetawearApp)
        self.buttonExit.setGeometry(QtCore.QRect(870, 360, 97, 27))
        self.buttonExit.setObjectName("buttonExit")
        self.secondsSpin = QtWidgets.QSpinBox(MetawearApp)
        self.secondsSpin.setGeometry(QtCore.QRect(430, 10, 60, 27))
        self.secondsSpin.setMinimum(1)
        self.secondsSpin.setObjectName("secondsSpin")
        self.label = QtWidgets.QLabel(MetawearApp)
        self.label.setGeometry(QtCore.QRect(500, 20, 66, 17))
        self.label.setObjectName("label")
        self.buttonDownloadData = QtWidgets.QPushButton(MetawearApp)
        self.buttonDownloadData.setGeometry(QtCore.QRect(30, 190, 121, 31))
        self.buttonDownloadData.setObjectName("buttonDownloadData")
        self.labelDownloadData = QtWidgets.QLabel(MetawearApp)
        self.labelDownloadData.setGeometry(QtCore.QRect(160, 200, 181, 17))
        self.labelDownloadData.setObjectName("labelDownloadData")
        self.nameText = QtWidgets.QLineEdit(MetawearApp)
        self.nameText.setGeometry(QtCore.QRect(100, 10, 301, 27))
        self.nameText.setObjectName("nameText")
        self.label_2 = QtWidgets.QLabel(MetawearApp)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 41, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MetawearApp)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MetawearApp)
        self.label_4.setGeometry(QtCore.QRect(370, 70, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.buttonResetDevice = QtWidgets.QPushButton(MetawearApp)
        self.buttonResetDevice.setGeometry(QtCore.QRect(30, 350, 131, 31))
        self.buttonResetDevice.setObjectName("buttonResetDevice")

        # added
        self.figure = Figure() 
        
        self.matplotlibFigure = QtWidgets.QWidget(MetawearApp)
        self.matplotlibFigure.setGeometry(QtCore.QRect(500, 80, 351, 301))
        self.matplotlibFigure.setObjectName("matplotlibFigure")
        self.buttonPlot = QtWidgets.QPushButton(MetawearApp)
        self.buttonPlot.setGeometry(QtCore.QRect(370, 110, 97, 31))
        self.buttonPlot.setObjectName("buttonPlot")

        self.retranslateUi(MetawearApp)
        QtCore.QMetaObject.connectSlotsByName(MetawearApp)

    def retranslateUi(self, MetawearApp):
        _translate = QtCore.QCoreApplication.translate
        MetawearApp.setWindowTitle(_translate("MetawearApp", "Metawear App"))
        self.buttonConnect.setText(_translate("MetawearApp", "Connect"))
        self.labelConnect.setText(_translate("MetawearApp", "..."))
        self.buttonGatherData.setText(_translate("MetawearApp", "Gather Data"))
        self.labelGatherData.setText(_translate("MetawearApp", "..."))
        self.buttonExit.setText(_translate("MetawearApp", "Exit"))
        self.label.setText(_translate("MetawearApp", "seconds"))
        self.buttonDownloadData.setText(_translate("MetawearApp", "Download Data"))
        self.labelDownloadData.setText(_translate("MetawearApp", "..."))
        self.label_2.setText(_translate("MetawearApp", "Name"))
        self.label_3.setText(_translate("MetawearApp", "Fixed Gather"))
        self.label_4.setText(_translate("MetawearApp", "Streaming"))
        self.buttonResetDevice.setText(_translate("MetawearApp", "Reset Device"))
        self.buttonPlot.setText(_translate("MetawearApp", "Plot"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MetawearApp = QtWidgets.QDialog()
    ui = Ui_MetawearApp()
    ui.setupUi(MetawearApp)
    MetawearApp.show()
    sys.exit(app.exec_())
