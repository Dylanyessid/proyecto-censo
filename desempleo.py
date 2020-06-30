# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desempleo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_desempleo(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(544, 465)
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
        self.cerrar.setGeometry(QtCore.QRect(510, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cerrar.setFont(font)
        self.cerrar.setObjectName("cerrar")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 481, 431))
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
        self.resultado = QtWidgets.QLabel(self.widget)
        self.resultado.setGeometry(QtCore.QRect(40, 350, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.resultado.setFont(font)
        self.resultado.setStyleSheet("color: #ff2121 ;")
        self.resultado.setText("")
        self.resultado.setObjectName("resultado")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(80, 20, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Region = QtWidgets.QLineEdit(self.widget)
        self.Region.setGeometry(QtCore.QRect(150, 70, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Region.setFont(font)
        self.Region.setMaxLength(15)
        self.Region.setObjectName("Region")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.CuadroDesempleados = QtWidgets.QLineEdit(self.widget)
        self.CuadroDesempleados.setGeometry(QtCore.QRect(150, 150, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CuadroDesempleados.setFont(font)
        self.CuadroDesempleados.setObjectName("CuadroDesempleados")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(80, 180, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.CuadroPoblacionAct = QtWidgets.QLineEdit(self.widget)
        self.CuadroPoblacionAct.setGeometry(QtCore.QRect(150, 250, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CuadroPoblacionAct.setFont(font)
        self.CuadroPoblacionAct.setObjectName("CuadroPoblacionAct")
        self.enviar = QtWidgets.QPushButton(self.widget)
        self.enviar.setGeometry(QtCore.QRect(150, 290, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.enviar.setFont(font)
        self.enviar.setObjectName("enviar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cerrar.setText(_translate("Dialog", "X"))
        self.label.setText(_translate("Dialog", "Ingrese el nombre del territorio:"))
        self.label_2.setText(_translate("Dialog", "Ingrese la cantidad de desempleados\n"
"en la región:"))
        self.label_3.setText(_translate("Dialog", "Ingrese len números la población activa \n"
" (la que está en condiciones de ejercer \n"
"algún trabajo):"))
        self.enviar.setText(_translate("Dialog", "Enviar"))
