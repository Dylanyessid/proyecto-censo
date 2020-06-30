# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'porcentajes.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_porcentajes(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 509)
        Dialog.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: #e53232;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"     background-color:white;\n"
"\n"
"}\n"
"\n"
"*{\n"
"background-color:#212323;\n"
"}")
        self.cerrar = QtWidgets.QPushButton(Dialog)
        self.cerrar.setGeometry(QtCore.QRect(470, 0, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cerrar.setFont(font)
        self.cerrar.setCheckable(False)
        self.cerrar.setObjectName("cerrar")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(50, 10, 391, 481))
        self.widget.setStyleSheet("*{    \n"
"    font-family: \"Century Gothic\";\n"
"    color:white ;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"    background-color:#48e848;\n"
"}")
        self.widget.setObjectName("widget")
        self.porc1 = QtWidgets.QLabel(self.widget)
        self.porc1.setGeometry(QtCore.QRect(30, 0, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.porc1.setFont(font)
        self.porc1.setText("")
        self.porc1.setObjectName("porc1")
        self.porc2 = QtWidgets.QLabel(self.widget)
        self.porc2.setGeometry(QtCore.QRect(30, 70, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.porc2.setFont(font)
        self.porc2.setText("")
        self.porc2.setObjectName("porc2")
        self.porc3 = QtWidgets.QLabel(self.widget)
        self.porc3.setGeometry(QtCore.QRect(30, 140, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.porc3.setFont(font)
        self.porc3.setText("")
        self.porc3.setObjectName("porc3")
        self.porc4 = QtWidgets.QLabel(self.widget)
        self.porc4.setGeometry(QtCore.QRect(30, 210, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.porc4.setFont(font)
        self.porc4.setText("")
        self.porc4.setObjectName("porc4")
        self.porc5 = QtWidgets.QLabel(self.widget)
        self.porc5.setGeometry(QtCore.QRect(30, 280, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.porc5.setFont(font)
        self.porc5.setText("")
        self.porc5.setObjectName("porc5")
        self.porc6 = QtWidgets.QLabel(self.widget)
        self.porc6.setGeometry(QtCore.QRect(30, 350, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.porc6.setFont(font)
        self.porc6.setText("")
        self.porc6.setObjectName("porc6")
        self.total = QtWidgets.QLabel(self.widget)
        self.total.setGeometry(QtCore.QRect(30, 420, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.total.setFont(font)
        self.total.setStyleSheet("background-color:#3595a0;")
        self.total.setText("")
        self.total.setObjectName("total")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cerrar.setText(_translate("Dialog", "X"))
