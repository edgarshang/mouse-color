# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mousecolor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(130, 70)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 16, 16))
        self.label_3.setObjectName("label_3")
        self.lbl_color_r = QtWidgets.QLabel(Form)
        self.lbl_color_r.setGeometry(QtCore.QRect(30, 10, 31, 16))
        self.lbl_color_r.setObjectName("lbl_color_r")
        self.lbl_color_g = QtWidgets.QLabel(Form)
        self.lbl_color_g.setGeometry(QtCore.QRect(30, 30, 31, 16))
        self.lbl_color_g.setObjectName("lbl_color_g")
        self.lbl_color_b = QtWidgets.QLabel(Form)
        self.lbl_color_b.setGeometry(QtCore.QRect(30, 50, 31, 16))
        self.lbl_color_b.setObjectName("lbl_color_b")
        self.tbcolor = QtWidgets.QTextBrowser(Form)
        self.tbcolor.setGeometry(QtCore.QRect(60, 10, 61, 41))
        self.tbcolor.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.tbcolor.setObjectName("tbcolor")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 50, 71, 21))
        self.label_4.setStyleSheet('font: 9pt "Eras Medium ITC";\n' "color: rgb(255, 0, 0);")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MsColor"))
        self.label.setText(_translate("Form", "R"))
        self.label_2.setText(_translate("Form", "G"))
        self.label_3.setText(_translate("Form", "B"))
        self.lbl_color_r.setText(_translate("Form", "255"))
        self.lbl_color_g.setText(_translate("Form", "255"))
        self.lbl_color_b.setText(_translate("Form", "255"))
        self.label_4.setText(_translate("Form", "By AlexShiDi"))
