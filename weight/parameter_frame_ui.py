# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/parameter_frame.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(535, 32)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(Frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.radioButton = QtWidgets.QRadioButton(Frame)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.lineEdit_2.setPlaceholderText(_translate("Frame", "变量名"))
        self.lineEdit.setPlaceholderText(_translate("Frame", "变量值"))
        self.radioButton.setText(_translate("Frame", "isNowTime"))
