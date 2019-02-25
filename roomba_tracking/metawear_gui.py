# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metawear.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(428, 247)
        self.buttonConnect = QtWidgets.QPushButton(Dialog)
        self.buttonConnect.setGeometry(QtCore.QRect(100, 50, 121, 31))
        self.buttonConnect.setObjectName("buttonConnect")
        self.labelConnect = QtWidgets.QLabel(Dialog)
        self.labelConnect.setGeometry(QtCore.QRect(230, 60, 181, 17))
        self.labelConnect.setObjectName("labelConnect")
        self.buttonGatherData = QtWidgets.QPushButton(Dialog)
        self.buttonGatherData.setGeometry(QtCore.QRect(100, 90, 121, 31))
        self.buttonGatherData.setObjectName("buttonGatherData")
        self.labelGatherData = QtWidgets.QLabel(Dialog)
        self.labelGatherData.setGeometry(QtCore.QRect(230, 100, 171, 17))
        self.labelGatherData.setObjectName("labelGatherData")
        self.buttonExit = QtWidgets.QPushButton(Dialog)
        self.buttonExit.setGeometry(QtCore.QRect(60, 200, 97, 27))
        self.buttonExit.setObjectName("buttonExit")
        self.secondsSpin = QtWidgets.QSpinBox(Dialog)
        self.secondsSpin.setGeometry(QtCore.QRect(30, 90, 60, 27))
        self.secondsSpin.setMinimum(1)
        self.secondsSpin.setObjectName("secondsSpin")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 120, 66, 17))
        self.label.setObjectName("label")
        self.buttonDownloadData = QtWidgets.QPushButton(Dialog)
        self.buttonDownloadData.setGeometry(QtCore.QRect(100, 130, 121, 31))
        self.buttonDownloadData.setObjectName("buttonDownloadData")
        self.labelDownloadData = QtWidgets.QLabel(Dialog)
        self.labelDownloadData.setGeometry(QtCore.QRect(230, 140, 181, 17))
        self.labelDownloadData.setObjectName("labelDownloadData")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.buttonConnect.setText(_translate("Dialog", "Connect"))
        self.labelConnect.setText(_translate("Dialog", "..."))
        self.buttonGatherData.setText(_translate("Dialog", "Gather Data"))
        self.labelGatherData.setText(_translate("Dialog", "..."))
        self.buttonExit.setText(_translate("Dialog", "Exit"))
        self.label.setText(_translate("Dialog", "seconds"))
        self.buttonDownloadData.setText(_translate("Dialog", "Download Data"))
        self.labelDownloadData.setText(_translate("Dialog", "..."))


