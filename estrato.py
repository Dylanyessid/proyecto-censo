# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estrato.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_estrato(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(641, 599)
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
        self.cerrar.setGeometry(QtCore.QRect(610, 0, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cerrar.setFont(font)
        self.cerrar.setObjectName("cerrar")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 601, 561))
        self.widget.setStyleSheet("QPushButton{\n"
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
"\n"
"*{\n"
"    background-color:  #323333  ;\n"
"    font-family: \"Century Gothic\";\n"
"    color:white ;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"\n"
"background-color:white;\n"
"color:black;\n"
"\n"
"}")
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 251, 161))
        self.groupBox.setStyleSheet("border:none;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.regulares = QtWidgets.QRadioButton(self.groupBox)
        self.regulares.setGeometry(QtCore.QRect(10, 80, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.regulares.setFont(font)
        self.regulares.setChecked(True)
        self.regulares.setObjectName("regulares")
        self.aceptables = QtWidgets.QRadioButton(self.groupBox)
        self.aceptables.setGeometry(QtCore.QRect(10, 110, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.aceptables.setFont(font)
        self.aceptables.setObjectName("aceptables")
        self.buenas = QtWidgets.QRadioButton(self.groupBox)
        self.buenas.setGeometry(QtCore.QRect(10, 140, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.buenas.setFont(font)
        self.buenas.setObjectName("buenas")
        self.muybuenas = QtWidgets.QRadioButton(self.groupBox)
        self.muybuenas.setGeometry(QtCore.QRect(110, 90, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.muybuenas.setFont(font)
        self.muybuenas.setObjectName("muybuenas")
        self.excelentes = QtWidgets.QRadioButton(self.groupBox)
        self.excelentes.setGeometry(QtCore.QRect(110, 130, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.excelentes.setFont(font)
        self.excelentes.setObjectName("excelentes")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 180, 251, 101))
        self.groupBox_2.setStyleSheet("border:none;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.conexionsi = QtWidgets.QRadioButton(self.groupBox_2)
        self.conexionsi.setGeometry(QtCore.QRect(10, 80, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.conexionsi.setFont(font)
        self.conexionsi.setObjectName("conexionsi")
        self.conexionno = QtWidgets.QRadioButton(self.groupBox_2)
        self.conexionno.setGeometry(QtCore.QRect(100, 80, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.conexionno.setFont(font)
        self.conexionno.setChecked(True)
        self.conexionno.setObjectName("conexionno")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 280, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.numh = QtWidgets.QLineEdit(self.widget)
        self.numh.setGeometry(QtCore.QRect(20, 350, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.numh.setFont(font)
        self.numh.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.numh.setText("")
        self.numh.setMaxLength(2)
        self.numh.setReadOnly(False)
        self.numh.setClearButtonEnabled(False)
        self.numh.setObjectName("numh")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(0, 380, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.nume = QtWidgets.QLineEdit(self.widget)
        self.nume.setGeometry(QtCore.QRect(20, 450, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.nume.setFont(font)
        self.nume.setMaxLength(3)
        self.nume.setObjectName("nume")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setGeometry(QtCore.QRect(290, 20, 261, 111))
        self.groupBox_3.setStyleSheet("border:none;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(60, 0, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.viassi = QtWidgets.QRadioButton(self.groupBox_3)
        self.viassi.setGeometry(QtCore.QRect(60, 80, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.viassi.setFont(font)
        self.viassi.setObjectName("viassi")
        self.viasno = QtWidgets.QRadioButton(self.groupBox_3)
        self.viasno.setGeometry(QtCore.QRect(170, 80, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.viasno.setFont(font)
        self.viasno.setChecked(True)
        self.viasno.setObjectName("viasno")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_4.setGeometry(QtCore.QRect(330, 120, 221, 121))
        self.groupBox_4.setStyleSheet("border:none;")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.garagesi = QtWidgets.QRadioButton(self.groupBox_4)
        self.garagesi.setGeometry(QtCore.QRect(30, 100, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.garagesi.setFont(font)
        self.garagesi.setObjectName("garagesi")
        self.garageno = QtWidgets.QRadioButton(self.groupBox_4)
        self.garageno.setGeometry(QtCore.QRect(120, 100, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.garageno.setFont(font)
        self.garageno.setChecked(True)
        self.garageno.setObjectName("garageno")
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_5.setGeometry(QtCore.QRect(240, 240, 361, 201))
        self.groupBox_5.setStyleSheet("border:none;")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(40, 10, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.ingreso1 = QtWidgets.QRadioButton(self.groupBox_5)
        self.ingreso1.setGeometry(QtCore.QRect(10, 90, 341, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ingreso1.setFont(font)
        self.ingreso1.setChecked(True)
        self.ingreso1.setObjectName("ingreso1")
        self.ingreso2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.ingreso2.setGeometry(QtCore.QRect(10, 120, 351, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ingreso2.setFont(font)
        self.ingreso2.setObjectName("ingreso2")
        self.ingreso3 = QtWidgets.QRadioButton(self.groupBox_5)
        self.ingreso3.setGeometry(QtCore.QRect(10, 150, 351, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ingreso3.setFont(font)
        self.ingreso3.setObjectName("ingreso3")
        self.ingreso4 = QtWidgets.QRadioButton(self.groupBox_5)
        self.ingreso4.setGeometry(QtCore.QRect(10, 180, 341, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ingreso4.setFont(font)
        self.ingreso4.setObjectName("ingreso4")
        self.enviar = QtWidgets.QPushButton(self.widget)
        self.enviar.setGeometry(QtCore.QRect(200, 460, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.enviar.setFont(font)
        self.enviar.setObjectName("enviar")
        self.error = QtWidgets.QLabel(self.widget)
        self.error.setGeometry(QtCore.QRect(20, 520, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.error.setFont(font)
        self.error.setStyleSheet("color:  #ff2121 ;")
        self.error.setText("")
        self.error.setObjectName("error")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cerrar.setText(_translate("Dialog", "X"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>¿Qué condiciones tiene </p><p>la vivienda y el entorno?</p></body></html>"))
        self.regulares.setText(_translate("Dialog", "Regulares"))
        self.aceptables.setText(_translate("Dialog", "Aceptables"))
        self.buenas.setText(_translate("Dialog", "Buenas"))
        self.muybuenas.setText(_translate("Dialog", "Muy Buenas"))
        self.excelentes.setText(_translate("Dialog", "Excelentes"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>¿Posee conexión</p><p> a Internet?</p></body></html>"))
        self.conexionsi.setText(_translate("Dialog", "Si"))
        self.conexionno.setText(_translate("Dialog", "No"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>¿Cuántas habitaciones</p><p>posee la vivienda?</p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>¿Cuántos electrodomésticos</p><p>hay en la vivienda?</p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p>¿Tiene acceso a</p><p>vías pavimentadas?</p></body></html>"))
        self.viassi.setText(_translate("Dialog", "Si"))
        self.viasno.setText(_translate("Dialog", "No"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p>¿La vivienda posee</p><p>un garage propio?</p></body></html>"))
        self.garagesi.setText(_translate("Dialog", "Si"))
        self.garageno.setText(_translate("Dialog", "No"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p>¿Cuál es el ingreso total</p><p>de los residentes de la vivienda?</p></body></html>"))
        self.ingreso1.setText(_translate("Dialog", "Menos de 1 Salario Mínimo Mensual Legal Vigente"))
        self.ingreso2.setText(_translate("Dialog", "Entre 1 y 2 Salarios Mínimos Mensual Legal Vigente"))
        self.ingreso3.setText(_translate("Dialog", "Entre 2 y 3 Salarios Mínimos Mensual Legal Vigente"))
        self.ingreso4.setText(_translate("Dialog", "4 o más Salarios Mínimos Mensual Legal Vigente"))
        self.enviar.setText(_translate("Dialog", "Enviar"))
