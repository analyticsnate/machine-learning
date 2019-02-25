# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metawear.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MetawearApp(object):
    def setupUi(self, MetawearApp):
        MetawearApp.setObjectName("MetawearApp")
        MetawearApp.resize(428, 247)
        self.buttonConnect = QtWidgets.QPushButton(MetawearApp)
        self.buttonConnect.setGeometry(QtCore.QRect(100, 50, 121, 31))
        self.buttonConnect.setObjectName("buttonConnect")
        self.labelConnect = QtWidgets.QLabel(MetawearApp)
        self.labelConnect.setGeometry(QtCore.QRect(230, 60, 181, 17))
        self.labelConnect.setObjectName("labelConnect")
        self.buttonGatherData = QtWidgets.QPushButton(MetawearApp)
        self.buttonGatherData.setGeometry(QtCore.QRect(100, 90, 121, 31))
        self.buttonGatherData.setObjectName("buttonGatherData")
        self.labelGatherData = QtWidgets.QLabel(MetawearApp)
        self.labelGatherData.setGeometry(QtCore.QRect(230, 100, 171, 17))
        self.labelGatherData.setObjectName("labelGatherData")
        self.buttonExit = QtWidgets.QPushButton(MetawearApp)
        self.buttonExit.setGeometry(QtCore.QRect(60, 200, 97, 27))
        self.buttonExit.setObjectName("buttonExit")
        self.secondsSpin = QtWidgets.QSpinBox(MetawearApp)
        self.secondsSpin.setGeometry(QtCore.QRect(30, 90, 60, 27))
        self.secondsSpin.setMinimum(1)
        self.secondsSpin.setObjectName("secondsSpin")
        self.label = QtWidgets.QLabel(MetawearApp)
        self.label.setGeometry(QtCore.QRect(30, 120, 66, 17))
        self.label.setObjectName("label")
        self.buttonDownloadData = QtWidgets.QPushButton(MetawearApp)
        self.buttonDownloadData.setGeometry(QtCore.QRect(100, 130, 121, 31))
        self.buttonDownloadData.setObjectName("buttonDownloadData")
        self.labelDownloadData = QtWidgets.QLabel(MetawearApp)
        self.labelDownloadData.setGeometry(QtCore.QRect(230, 140, 181, 17))
        self.labelDownloadData.setObjectName("labelDownloadData")
        self.nameText = QtWidgets.QLineEdit(MetawearApp)
        self.nameText.setGeometry(QtCore.QRect(100, 10, 301, 27))
        self.nameText.setObjectName("nameText")
        self.label_2 = QtWidgets.QLabel(MetawearApp)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 41, 20))
        self.label_2.setObjectName("label_2")

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


