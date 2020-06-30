# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'est.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_est(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(487, 375)
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
        self.cerrar.setGeometry(QtCore.QRect(450, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cerrar.setFont(font)
        self.cerrar.setObjectName("cerrar")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 20, 411, 331))
        self.widget.setStyleSheet("*{\n"
"    background-color:  #323333  ;\n"
"    font-family: \"Century Gothic\";\n"
"    color:white ;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"    background-color:#3595a0;;\n"
"\n"
"\n"
"}")
        self.widget.setObjectName("widget")
        self.titulo = QtWidgets.QLabel(self.widget)
        self.titulo.setGeometry(QtCore.QRect(120, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.descripcion = QtWidgets.QLabel(self.widget)
        self.descripcion.setGeometry(QtCore.QRect(10, 80, 391, 111))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.descripcion.setFont(font)
        self.descripcion.setObjectName("descripcion")
        self.descripcion_2 = QtWidgets.QLabel(self.widget)
        self.descripcion_2.setGeometry(QtCore.QRect(20, 220, 371, 101))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.descripcion_2.setFont(font)
        self.descripcion_2.setStyleSheet("background-color:   #dc0707;")
        self.descripcion_2.setObjectName("descripcion_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cerrar.setText(_translate("Dialog", "X"))
        self.titulo.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Estrato 1</p></body></html>"))
        self.descripcion.setText(_translate("Dialog", "Este es el estrato más bajo: Bajo-bajo. Las  \n"
"condiciones de la casa al igual que el entorno\n"
" que le rodea poseen pocos lujos. Los habitantes\n"
" que poseen este estrato pueden recibir subsidios"))
        self.descripcion_2.setText(_translate("Dialog", "Advertencia: Los resultados obtenidos son\n"
" aproximaciones. NO son datos totalmente\n"
" seguros ni acertados,ya que el resultado\n"
" puede llegar a errores dependiendo de\n"
" los parámetros reales."))
