import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

#Clase Constructor de ventanas
class Menu(QMainWindow):

    #Constructor de la clase
    def __init__(self):

        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)

        #Cargar la configuracion .ui
        uic.loadUi("menu.ui",self)

#Inicializa la aplicacion
app=QApplication(sys.argv)

#Crea un objeto de la clase Menu
menu=Menu()

#Muestra la ventana
menu.show()

#Ejecuta la aplicacion
app.exec()
