import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
import ctypes
from PyQt5.QtCore import *
from menu import *
from estrato import *
from est import *
from desempleo import *
from densidad import *
from cant_estrato import *
from porcentajes import *

#Clase Constructor de ventanas
class Menu(QMainWindow):



    #Constructor de la clase
    def __init__(self):

        #Iniciar el objeto QMainWindow y sus configuraciones
        QMainWindow.__init__(self)

        self.ui=Ui_CENSO()
        self.ui.setupUi(self)

        self.setFixedSize(607, 487)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("logo.ico"))


        #Cargar la configuracion .ui


        #Programa el cerrado del programa y un botón que lo ejecuta.
        def CerrarPrincipal(self):
            QCoreApplication.instance().quit()

        #Conecta el boton con la ventana para calcular el estrato
        def ConectarEst(self):
            VentanaEst=Ventana1()
            VentanaEst.exec()

        #Conecta el boton con la ventana para calcular la tasa de desempleo
        def ConectarDes(self):
            VentanaDes=Ventana2()
            VentanaDes.exec()

        #Conecta el boton con la ventana para calcular la densidad de población
        def ConectarDen(self):
            VentanaDen=Ventana3()
            VentanaDen.exec()

        #Conecta el boton con la ventana para calcular los porcentajes de cada estrato
        def ConectarCantEst(self):
            VentanaCantEst=Ventana4()
            VentanaCantEst.exec()






        #Botones y su configuración
        self.ui.cerrar_principal.clicked.connect(CerrarPrincipal)
        self.ui.BotonEst.clicked.connect(ConectarEst)
        self.ui.BotonDes.clicked.connect(ConectarDes)
        self.ui.BotonDen.clicked.connect(ConectarDen)
        self.ui.BotonCantEst.clicked.connect(ConectarCantEst)

#Define la Ventana para calcular el estrato de una vivienda
class Ventana1(QDialog):
    def __init__(self):

        #Inicializa el objetto (Ventana)
        QDialog.__init__(self)

        #Configuraciones de la ventana
        self.ui = Ui_estrato()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui.numh.setAlignment(Qt.AlignCenter)
        self.ui.nume.setAlignment(Qt.AlignCenter)
        self.ui.error.setAlignment(Qt.AlignCenter)


        #Botones y configuracion
        self.ui.cerrar.clicked.connect(self.close)
        self.ui.enviar.clicked.connect(self.EnviarDatosEst)

        #Enntrada de linea de texto y configuracion
        self.ui.numh.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.ui.nume.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")



        #Funcion que procesa los datos
    def EnviarDatosEst(self):

        #Obtención de datos de linea de texto
        NumHabitaciones = self.ui.numh.text()
        NumElectro = self.ui.nume.text()



        try:
        #Condicionales para asignar valores con respecto al RadioButton seleccionado
            if self.ui.regulares.isChecked():
                Condiciones=2
            elif self.ui.aceptables.isChecked():
                Condiciones=4
            elif self.ui.buenas.isChecked():
                Condiciones=8
            elif self.ui.muybuenas.isChecked():
                Condiciones=12
            elif self.ui.excelentes.isChecked():
                Condiciones=14

            if self.ui.conexionsi.isChecked():
                OpcionInternet=4
            elif self.ui.conexionno.isChecked():
                OpcionInternet=0

            if self.ui.viassi.isChecked():
                OpcionVia=4
            elif self.ui.conexionno.isChecked():
                OpcionVia=1

            if self.ui.garagesi.isChecked():
                OpcionGarage=5
            elif self.ui.garageno.isChecked():
                OpcionGarage=1

            if self.ui.ingreso1.isChecked():
                Ingreso=2
            elif self.ui.ingreso2.isChecked():
                Ingreso=5
            elif self.ui.ingreso3.isChecked():
                Ingreso=7
            elif self.ui.ingreso4.isChecked():
                Ingreso=9

            #Condicion que se activa cuando los valores son válidos
            if float(NumElectro)>0 and float(NumHabitaciones)>0:

                #Calcula la suma entre todos los datos obtenidos
                CondicionesVivienda=int(Condiciones) + int(OpcionInternet) + int(NumHabitaciones) + int(NumElectro) + int(OpcionVia) + int(OpcionGarage) + int(Ingreso)

                #Cierra la ventana
                self.close()

            #Condiciones con respecto al valor total obtenido que abre una ventana con datos diferentes.
                if CondicionesVivienda>0 and CondicionesVivienda<=23:

                    VEst=Est1()
                    VEst.exec()


                elif CondicionesVivienda>23 and CondicionesVivienda<=35:

                    VEst2=Est2()
                    VEst2.exec()

                elif CondicionesVivienda>35 and CondicionesVivienda<=48:

                    VEst3=Est3()
                    VEst3.exec()

                elif CondicionesVivienda>48 and CondicionesVivienda<=59:

                    VEst4=Est4()
                    VEst4.exec()

                elif CondicionesVivienda>59 and CondicionesVivienda<=70:

                    VEst5=Est5()
                    VEst5.exec()

                elif CondicionesVivienda>70:

                    VEst6=Est6()
                    VEst6.exec()

            else:
                #Si se ingresa numeros negativos
                self.ui.error.setText("No es posible ingresar números negativos")

        except ValueError:
            #Si se introduce datos inválidos
            self.ui.error.setText("Ha ingresado un dato inválido, inténtalo de nuevo")



#Configuraciones de ventana de resultado para Estrato 1
class Est1(QDialog):
    def __init__(self):

        #Inicializa Ventana y sus configuraciones
        QDialog.__init__(self)
        self.ui = Ui_est()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.ui.cerrar.clicked.connect(self.close)

#Configuraciones de ventana de resultado para Estrato 2
class Est2(QDialog):
    def __init__(self):

        #Inicializa Ventana y sus configuraciones
        QDialog.__init__(self)
        self.ui = Ui_est()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.ui.cerrar.clicked.connect(self.close)

        self.ui.titulo.setText("Estrato 2")
        self.ui.titulo.setAlignment(Qt.AlignCenter)

        self.ui.descripcion.setText("Este es el estrato: Bajo. Las condiciones de la casa\nal igual que en el entorno son un poco mejores.\n Este estrato tambien pueden recibir subsidios.")

#Configuraciones de ventana de resultado para Estrato 3
class Est3(QDialog):
    def __init__(self):

        #Inicializa Ventana y sus configuraciones
        QDialog.__init__(self)
        self.ui = Ui_est()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.ui.cerrar.clicked.connect(self.close)


        self.ui.titulo.setText("Estrato 3")
        self.ui.titulo.setAlignment(Qt.AlignCenter)
        self.ui.descripcion.setText("Este estrato corresponde a: Medio-bajo. Las\ncondiciones en las que se vive son considerables.\nEste estrato es el más alto en el que\nse pueden recibir subsidios")

#Configuraciones de ventana de resultado para Estrato 4
class Est4(QDialog):
    def __init__(self):

        #Inicializa Ventana y sus configuraciones
        QDialog.__init__(self)
        self.ui = Ui_est()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.ui.cerrar.clicked.connect(self.close)


        self.ui.titulo.setText("Estrato 4")
        self.ui.titulo.setAlignment(Qt.AlignCenter)
        self.ui.descripcion.setText("Este estrato corresponde a: Medio.\nUna característica de este estrato es que no\npuede recibir subsidios(como los más bajos)\nni tienen que pagar sobrecostos\n(como los más altos).")

#Configuraciones de ventana de resultado para Estrato 5
class Est5(QDialog):
    def __init__(self):

        #Inicializa Ventana y sus configuraciones
        QDialog.__init__(self)
        self.ui = Ui_est()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.ui.cerrar.clicked.connect(self.close)

        self.ui.titulo.setText("Estrato 5")
        self.ui.titulo.setAlignment(Qt.AlignCenter)
        self.ui.descripcion.setText("Este estrato corresponde a: Medio-alto.\nA partir de este estrato se debe de pagar\nsobrecostos en los servicios públicos\ncomo contribución ya que suelen\ntener mayores recursos económicos.")

#Configuraciones de ventana de resultado para Estrato 6
class Est6(QDialog):
    def __init__(self):

        #Inicializa Ventana y sus configuraciones
        QDialog.__init__(self)
        self.ui = Ui_est()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.ui.cerrar.clicked.connect(self.close)


        self.ui.titulo.setText("Estrato 6")
        self.ui.titulo.setAlignment(Qt.AlignCenter)
        self.ui.descripcion.setText("Este estrato corresponde a: Alto. \nEs el estrato socioeconómico más alto. Poseen\nexcelentes condiciones tanto de vivienda\ncomo de entorno y también paga\nsobrecostos en los servicios públicos.")

#Ventana para calcular la tasa de desempleo
class Ventana2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_desempleo()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.ui.cerrar.clicked.connect(self.close)
        self.ui.enviar.clicked.connect(self.EnviarDatosDes)

        #Configuraciones de entrada de ttexto
        self.ui.Region.setAlignment(Qt.AlignCenter)
        self.ui.CuadroDesempleados.setAlignment(Qt.AlignCenter)
        self.ui.CuadroPoblacionAct.setAlignment(Qt.AlignCenter)
        self.ui.resultado.setAlignment(Qt.AlignCenter)

    #Funcion que prrocesa los datos
    def EnviarDatosDes(self):

        #Obtención de datos
        NombreTerritorio = self.ui.Region.text()
        NumDesempleados = self.ui.CuadroDesempleados.text()
        PoblacionAct = self.ui.CuadroPoblacionAct.text()


        try:

            #Intentar calcular el dato deseado
            TasaDesempleo=(int(NumDesempleados)/int(PoblacionAct)) * 100

            #Si el dato de la region esta vacio
            if NombreTerritorio=="":

                self.ui.resultado.setText("No puedes dejar vacío el nombre de la región")

            #Si los datos son correctos
            elif int(NumDesempleados)<=int(PoblacionAct) and int(NumDesempleados)>=0 and int(PoblacionAct)>=0:

                self.ui.resultado.setText("La tasa de desempleo en " + NombreTerritorio.upper() + " es de: \n % " + str(round(TasaDesempleo,2)))

            #Si los desempleados es mayor que la poblacion activa
            elif (int(NumDesempleados)>int(PoblacionAct)):

                self.ui.resultado.setText("El Numero de desempleados no\npuede ser mayor que la población")

            #Si no se cumple ninguna se asume que son negativos los numeros
            else:

                self.ui.resultado.setText("No es posible ingresar números negativos")



        #Por si ingresa datos invalidos
        except ValueError:

            self.ui.resultado.setText("Ha ingresado un dato inválido, inténtalo de nuevo")

        #Por si ingresa un 0, causando error matematico
        except ZeroDivisionError:

            self.ui.resultado.setText("No puedes introducir un\nnúmero 0 en la población activa")

#Clase de la ventana de Calcular densidad
class Ventana3(QDialog):
    def __init__(self):

        #Inicializa Ventana y sus configuraciones
        QDialog.__init__(self)
        self.ui = Ui_densidad()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.ui.cerrar.clicked.connect(self.close)
        self.ui.enviar.clicked.connect(self.EnviarDatosDen)

        #Estilos y configuraciones para las entradas de lineas de texto
        self.ui.Region.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.ui.CuadroPob.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.ui.CuadroSup.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")

        self.ui.resultado.setAlignment(Qt.AlignCenter)
        self.ui.Region.setAlignment(Qt.AlignCenter)
        self.ui.CuadroPob.setAlignment(Qt.AlignCenter)
        self.ui.CuadroSup.setAlignment(Qt.AlignCenter)


        #Funcion que procesa los datoa
    def EnviarDatosDen(self):

        #Obtención de datos
        NombreTerritorio = self.ui.Region.text()
        PoblacionTotal= self.ui.CuadroPob.text()
        Superficie= self.ui.CuadroSup.text()

        try:

            #Intentar calcular los datos solicitados
            DensidadPoblacion=int(PoblacionTotal) / float(Superficie)

            #Si el dato de la region esta vacio
            if NombreTerritorio=="":

                self.ui.resultado.setText("No puedes dejar vacío el nombre de la región")

            #Si los datos son correctos
            elif int(PoblacionTotal)>0 and float(Superficie)>0:

                self.ui.resultado.setText("La densidad de población de \n " +str(NombreTerritorio.upper()) +  " es de "+ str(round(DensidadPoblacion,2)) + "\n personas por kilómetro cuadrado.")

            #Si los datos son negativos
            elif int(PoblacionTotal)<0 or float(Superficie)<0:

                self.ui.resultado.setText("No puedes llenar los datos\ncon números negativos.")

            #Si se ingresa un 0.
            elif int(PoblacionTotal)==0:

                self.ui.resultado.setText("No puedes llenar los espacios\ncon 0. Reinténtalo" )

        #Si se ingresan datos no válidos
        except ValueError:

            self.ui.resultado.setText("Has ingresado incorrectamente\nlos datos. Reinténtalo")

        #Si se provoca un error por division entre 0
        except ZeroDivisionError:

            self.ui.resultado.setText("No puedes introducir 0 en los espacios" )

#Clase que define la ventana para los porcentajes de estrato
class Ventana4(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.ui = Ui_cant_estrato()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.ui.cerrar.clicked.connect(self.close)
        self.ui.enviar.clicked.connect(self.CalcularPorcentaje)

        #Estilos y configuraciones para las entradas de lineas de texto
        self.ui.Region.setAlignment(Qt.AlignCenter)
        self.ui.est1.setAlignment(Qt.AlignCenter)
        self.ui.est2.setAlignment(Qt.AlignCenter)
        self.ui.est3.setAlignment(Qt.AlignCenter)
        self.ui.est4.setAlignment(Qt.AlignCenter)
        self.ui.est5.setAlignment(Qt.AlignCenter)
        self.ui.est6.setAlignment(Qt.AlignCenter)

        self.ui.error.setAlignment(Qt.AlignCenter)



    #Funcion que procesa los datos
    def CalcularPorcentaje(self):

        try:

        #Convierte en Globales
            global NombreTerritorio
            global Estrato
            global Porcentaje
            global TotalEst

            #Obtencion de datos y creacion de vectores
            NombreTerritorio = self.ui.Region.text()
            Estrato=[]
            Porcentaje=[]

            #Adicion de datos al primer vector con respecto a los datos ingresados
            Estrato.append(self.ui.est1.text())
            Estrato.append(self.ui.est2.text())
            Estrato.append(self.ui.est3.text())
            Estrato.append(self.ui.est4.text())
            Estrato.append(self.ui.est5.text())
            Estrato.append(self.ui.est6.text())

            #Si los datos son negativos
            if int(Estrato[0])<0 or int(Estrato[1])<0 or int(Estrato[2])<0 or int(Estrato[3])<0 or int(Estrato[4])<0 or int(Estrato[5])<0:


                self.ui.error.setText("Ha ingresado un o más números negativos.\nReinténtalo")

            #Si el nombre de la region esta vacia.
            if NombreTerritorio=="":

                self.ui.error.setText("No puedes dejar vacío el nombre de la región")

            #Si son válidos los datos
            else:

                #Si los numeros son positivos
                if int(Estrato[0])>=0 and int(Estrato[1])>=0 and int(Estrato[2])>=0 and int(Estrato[3])>=0 and int(Estrato[4])>=0 and int(Estrato[5])>=0:
                    TotalEst=int(Estrato[0])+int(Estrato[1])+int(Estrato[2])+int(Estrato[3])+int(Estrato[4])+int(Estrato[5])

                    #Bucle for que agrega valores al segundo vector
                    for i in [0,1,2,3,4,5]:
                        Porcentaje.append((100 * float(Estrato[i]))/float(TotalEst))

                    #Cerrar esta ventana y abrir otra que muestre los resultados
                    self.close()
                    ResultadoPorc = Porcentajes()
                    ResultadoPorc.exec()





        #Si ingresa datos inválidos
        except ValueError:

            self.ui.error.setText("Has ingresado incorrectamente\nlos datos. Reinténtalo")

        #Si se provoca un error de division entre 0
        except ZeroDivisionError:

            self.ui.error.setText("No puedes introducir 0 en los espacios" )

#Clase que define la ventana de resultado de los porcentajes de estrato
class Porcentajes(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_porcentajes()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.ui.cerrar.clicked.connect(self.close)

        #Configuraciones de los textos
        self.ui.porc1.setAlignment(Qt.AlignCenter)
        self.ui.porc2.setAlignment(Qt.AlignCenter)
        self.ui.porc3.setAlignment(Qt.AlignCenter)
        self.ui.porc4.setAlignment(Qt.AlignCenter)
        self.ui.porc5.setAlignment(Qt.AlignCenter)
        self.ui.porc6.setAlignment(Qt.AlignCenter)
        self.ui.total.setAlignment(Qt.AlignCenter)

        self.ui.porc1.setText("El Porcentaje del Estrato 1 en\n " + str(NombreTerritorio.upper()) + "\nes de %" + str(round(Porcentaje[0],2)))
        self.ui.porc2.setText("El Porcentaje del Estrato 2 en\n " + str(NombreTerritorio.upper()) + "\nes de %" + str(round(Porcentaje[1],2)))
        self.ui.porc3.setText("El Porcentaje del Estrato 3 en\n " + str(NombreTerritorio.upper()) + "\nes de %" + str(round(Porcentaje[2],2)))
        self.ui.porc4.setText("El Porcentaje del Estrato 4 en\n " + str(NombreTerritorio.upper()) + "\nes de %" + str(round(Porcentaje[3],2)))
        self.ui.porc5.setText("El Porcentaje del Estrato 5 en\n " + str(NombreTerritorio.upper()) + "\nes de %" + str(round(Porcentaje[4],2)))
        self.ui.porc6.setText("El Porcentaje del Estrato 6 en\n " + str(NombreTerritorio.upper()) + "\nes de %" + str(round(Porcentaje[5],2)))

        self.ui.total.setText("El total de viviendas en\n" + str(NombreTerritorio.upper()) + "\nes de: " + str(TotalEst) )


#Inicializa la aplicacion principal
app=QApplication(sys.argv)

#Crea un objeto de la clase Menu
menu=Menu()

#Muestra la ventana
menu.show()

#Ejecuta la aplicacion
app.exec()
