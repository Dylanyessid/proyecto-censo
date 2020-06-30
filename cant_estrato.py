# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cant_estrato.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(542, 490)
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
"\n"
"*{\n"
"background-color:#212323;\n"
"}")
        self.cerrar = QtWidgets.QPushButton(Dialog)
        self.cerrar.setGeometry(QtCore.QRect(510, 0, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cerrar.setFont(font)
        self.cerrar.setObjectName("cerrar")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 10, 481, 461))
        self.widget.setStyleSheet("*{\n"
"    background-color:  #323333  ;\n"
"    font-family: \"Century Gothic\";\n"
"    color:white ;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:  #3595a0;\n"
"    border:none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    color: black;\n"
"    background-color: #f9f32d;\n"
"    }    \n"
"\n"
"QLineEdit{\n"
"\n"
"background-color:white;\n"
"color:black;\n"
"\n"
"}")
        self.widget.setObjectName("widget")
        self.Region = QtWidgets.QLineEdit(self.widget)
        self.Region.setGeometry(QtCore.QRect(140, 50, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Region.setFont(font)
        self.Region.setMaxLength(15)
        self.Region.setObjectName("Region")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(80, 20, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.enviar = QtWidgets.QPushButton(self.widget)
        self.enviar.setGeometry(QtCore.QRect(160, 360, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.enviar.setFont(font)
        self.enviar.setObjectName("enviar")
        self.est1 = QtWidgets.QLineEdit(self.widget)
        self.est1.setGeometry(QtCore.QRect(10, 140, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.est1.setFont(font)
        self.est1.setObjectName("est1")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.est2 = QtWidgets.QLineEdit(self.widget)
        self.est2.setGeometry(QtCore.QRect(10, 230, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.est2.setFont(font)
        self.est2.setObjectName("est2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.est3 = QtWidgets.QLineEdit(self.widget)
        self.est3.setGeometry(QtCore.QRect(10, 320, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.est3.setFont(font)
        self.est3.setObjectName("est3")
        self.est4 = QtWidgets.QLineEdit(self.widget)
        self.est4.setGeometry(QtCore.QRect(260, 140, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.est4.setFont(font)
        self.est4.setObjectName("est4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(260, 80, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.est5 = QtWidgets.QLineEdit(self.widget)
        self.est5.setGeometry(QtCore.QRect(270, 230, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.est5.setFont(font)
        self.est5.setObjectName("est5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(260, 170, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(260, 260, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.est6 = QtWidgets.QLineEdit(self.widget)
        self.est6.setGeometry(QtCore.QRect(270, 320, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.est6.setFont(font)
        self.est6.setObjectName("est6")
        self.error = QtWidgets.QLabel(self.widget)
        self.error.setGeometry(QtCore.QRect(30, 410, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.error.setFont(font)
        self.error.setStyleSheet("color: #ff2121 ;")
        self.error.setText("")
        self.error.setObjectName("error")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cerrar.setText(_translate("Dialog", "X"))
        self.label.setText(_translate("Dialog", "Ingrese el nombre del territorio:"))
        self.enviar.setText(_translate("Dialog", "Enviar"))
        self.label_2.setText(_translate("Dialog", "Ingrese la cantidad de\n"
"viviendas en estrato 1\n"
"del territorio:"))
        self.label_3.setText(_translate("Dialog", "Ingrese la cantidad de\n"
"viviendas en estrato 2\n"
"del territorio:"))
        self.label_4.setText(_translate("Dialog", "Ingrese la cantidad de\n"
"viviendas en estrato 3\n"
"del territorio:"))
        self.label_5.setText(_translate("Dialog", "Ingrese la cantidad de\n"
"viviendas en estrato 4\n"
"del territorio:"))
        self.label_6.setText(_translate("Dialog", "Ingrese la cantidad de\n"
"viviendas en estrato 5\n"
"del territorio:"))
        self.label_7.setText(_translate("Dialog", "Ingrese la cantidad de\n"
"viviendas en estrato 6\n"
"del territorio:"))
