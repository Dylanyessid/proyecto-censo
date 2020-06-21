import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import ctypes
from PyQt5.QtCore import Qt

#Clase Constructor de ventanas
class Menu(QMainWindow):

    #Constructor de la clase
    def __init__(self):

        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        self.setFixedSize(627, 500)

        #Cargar la configuracion .ui
        uic.loadUi("menu.ui",self)

        #Estilos CSS
        self.setStyleSheet("background-color: #5ae9f2")
        self.BotonEst.setStyleSheet("background-color:white")
        self.BotonDes.setStyleSheet("background-color:white")
        self.BotonDen.setStyleSheet("background-color:white")
        self.BotonCantEst.setStyleSheet("background-color:white")

    def closeEvent(self, event):
      resultado = QMessageBox.question(self, "Salir ...", "¿Seguro que quieres salir de la aplicación?", QMessageBox.Yes | QMessageBox.No)


      if resultado == QMessageBox.Yes:
          event.accept()
      else:
           event.ignore()







#Inicializa la aplicacion
app=QApplication(sys.argv)

#Crea un objeto de la clase Menu
menu=Menu()

#Muestra la ventana
menu.show()

#Ejecuta la aplicacion
app.exec()
