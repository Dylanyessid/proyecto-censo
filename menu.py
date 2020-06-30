# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CENSO(object):
    def setupUi(self, CENSO):
        CENSO.setObjectName("CENSO")
        CENSO.setWindowModality(QtCore.Qt.NonModal)
        CENSO.setEnabled(True)
        CENSO.resize(607, 487)
        CENSO.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        CENSO.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        CENSO.setLayoutDirection(QtCore.Qt.LeftToRight)
        CENSO.setAutoFillBackground(False)
        CENSO.setStyleSheet("QPushButton{\n"
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
        CENSO.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        CENSO.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(CENSO)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 20, 441, 451))
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
"    }    ")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(90, 20, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.BotonDes = QtWidgets.QPushButton(self.widget)
        self.BotonDes.setGeometry(QtCore.QRect(250, 260, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.BotonDes.setFont(font)
        self.BotonDes.setMouseTracking(False)
        self.BotonDes.setAutoFillBackground(False)
        self.BotonDes.setObjectName("BotonDes")
        self.BotonCantEst = QtWidgets.QPushButton(self.widget)
        self.BotonCantEst.setGeometry(QtCore.QRect(250, 350, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.BotonCantEst.setFont(font)
        self.BotonCantEst.setAutoFillBackground(False)
        self.BotonCantEst.setObjectName("BotonCantEst")
        self.BotonEst = QtWidgets.QPushButton(self.widget)
        self.BotonEst.setEnabled(True)
        self.BotonEst.setGeometry(QtCore.QRect(40, 260, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.BotonEst.setFont(font)
        self.BotonEst.setAutoFillBackground(False)
        self.BotonEst.setStyleSheet("")
        self.BotonEst.setFlat(False)
        self.BotonEst.setObjectName("BotonEst")
        self.BotonDen = QtWidgets.QPushButton(self.widget)
        self.BotonDen.setGeometry(QtCore.QRect(40, 350, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.BotonDen.setFont(font)
        self.BotonDen.setAutoFillBackground(False)
        self.BotonDen.setObjectName("BotonDen")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.cerrar_principal = QtWidgets.QPushButton(self.centralwidget)
        self.cerrar_principal.setGeometry(QtCore.QRect(570, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.cerrar_principal.setFont(font)
        self.cerrar_principal.setStyleSheet("")
        self.cerrar_principal.setObjectName("cerrar_principal")
        CENSO.setCentralWidget(self.centralwidget)

        self.retranslateUi(CENSO)
        QtCore.QMetaObject.connectSlotsByName(CENSO)

    def retranslateUi(self, CENSO):
        _translate = QtCore.QCoreApplication.translate
        CENSO.setWindowTitle(_translate("CENSO", "CENSO"))
        self.label.setText(_translate("CENSO", "<html><head/><body><p><span style=\" font-size:14pt;\">Bienvenido al sistema CENSO</span></p></body></html>"))
        self.BotonDes.setText(_translate("CENSO", "Calcular Tasa \n"
"de Desempleo"))
        self.BotonCantEst.setText(_translate("CENSO", "Calcular Porcentaje \n"
" de Estratos"))
        self.BotonEst.setText(_translate("CENSO", "Calcular Estrato\n"
"de una Vivienda"))
        self.BotonDen.setText(_translate("CENSO", "Calcular Densidad \n"
"de Desempleo"))
        self.label_2.setText(_translate("CENSO", "<html><head/><body><p><span style=\" font-size:14pt;\">Escoja la opción a realizar:</span></p></body></html>"))
        self.cerrar_principal.setText(_translate("CENSO", "X"))
