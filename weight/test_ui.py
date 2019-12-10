# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/test.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(206, 32)
        self.radioButton = QtWidgets.QRadioButton(Frame)
        self.radioButton.setGeometry(QtCore.QRect(110, 10, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 104, 31))
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.radioButton.setText(_translate("Frame", "RadioButton"))
