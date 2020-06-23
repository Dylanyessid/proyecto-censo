import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
import ctypes
from PyQt5.QtCore import *


#Clase Constructor de ventanas
class Menu(QMainWindow):



    #Constructor de la clase
    def __init__(self):

        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        self.setFixedSize(627, 500)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)


        #Cargar la configuracion .ui
        uic.loadUi("menu.ui",self)

        #Programa el cerrado del programa y un botón que lo ejecuta.
        def CerrarPrincipal(self):
            QCoreApplication.instance().quit()

        def ConectarEst(self):
            VentanaEst=Ventana1()
            VentanaEst.exec()

        def ConectarDes(self):
            VentanaDes=Ventana2()
            VentanaDes.exec()

        def ConectarDen(self):
            VentanaDen=Ventana3()
            VentanaDen.exec()

        def ConectarCantEst(self):
            VentanaCantEst=Ventana4()
            VentanaCantEst.exec()

        #Estilos CSS
        self.setStyleSheet("background-color: #5ae9f2")




        self.cerrar_principal.setStyleSheet("background-color:white")
        self.cerrar_principal.clicked.connect(CerrarPrincipal)

        #Botones
        self.BotonEst.setStyleSheet("background-color:white")
        self.BotonEst.clicked.connect(ConectarEst)

        self.BotonDes.setStyleSheet("background-color:white")
        self.BotonDes.clicked.connect(ConectarDes)

        self.BotonDen.setStyleSheet("background-color:white")
        self.BotonDen.clicked.connect(ConectarDen)

        self.BotonCantEst.setStyleSheet("background-color:white")
        self.BotonCantEst.clicked.connect(ConectarCantEst)


class Ventana1(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        uic.loadUi("estrato.ui",self)




        #Botones
        self.cerrar.clicked.connect(self.close)
        self.cerrar.setStyleSheet("background-color:white")
        self.setStyleSheet("background-color: #5ae9f2")

        self.entradahab.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.entradaelectro.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")

        self.enviar.clicked.connect(self.EnviarDatosEst)

    def EnviarDatosEst(self):
        hab = self.entradahab.text()
        ele = self.entradaelectro.text()
        print(hab)
        print(ele)






class Ventana2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("desempleo.ui",self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.cerrar.clicked.connect(self.close)
        self.cerrar.setStyleSheet("background-color:white")
        self.setStyleSheet("background-color: #5ae9f2")

class Ventana3(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("densidad.ui",self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.cerrar.clicked.connect(self.close)
        self.cerrar.setStyleSheet("background-color:white")
        self.setStyleSheet("background-color: #5ae9f2")

class Ventana4(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("densidad.ui",self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.cerrar.clicked.connect(self.close)
        self.cerrar.setStyleSheet("background-color:white")
        self.setStyleSheet("background-color: #5ae9f2")


#Inicializa la aplicacion
app=QApplication(sys.argv)

#Crea un objeto de la clase Menu
menu=Menu()

#Muestra la ventana
menu.show()

#Ejecuta la aplicacion
app.exec()
