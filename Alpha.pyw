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


#Clase Constructor de ventanas
class Menu(QMainWindow):



    #Constructor de la clase
    def __init__(self):

        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)

        self.ui=Ui_CENSO()
        self.ui.setupUi(self)

        self.setFixedSize(607, 487)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)


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

        #Estilos CSS




        #Botones y su configuración
        self.ui.cerrar_principal.clicked.connect(CerrarPrincipal)


        self.ui.BotonEst.clicked.connect(ConectarEst)


        self.ui.BotonDes.clicked.connect(ConectarDes)


        self.ui.BotonDen.clicked.connect(ConectarDen)


        self.ui.BotonCantEst.clicked.connect(ConectarCantEst)


class Ventana1(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.ui = Ui_estrato()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui.numh.setAlignment(Qt.AlignCenter)
        self.ui.nume.setAlignment(Qt.AlignCenter)
        self.ui.error.setAlignment(Qt.AlignCenter)


        #Botones
        self.ui.cerrar.clicked.connect(self.close)


        self.ui.numh.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.ui.nume.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")

        self.ui.enviar.clicked.connect(self.EnviarDatosEst)




    def EnviarDatosEst(self):



        NumHabitaciones = self.ui.numh.text()
        NumElectro = self.ui.nume.text()
        #print(int(NumHabitaciones))
        #print(int(NumElectro))


        try:
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


            if float(NumElectro)>0 and float(NumHabitaciones)>0:
                CondicionesVivienda=int(Condiciones) + int(OpcionInternet) + int(NumHabitaciones) + int(NumElectro) + int(OpcionVia) + int(OpcionGarage) + int(Ingreso)
                self.close()

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

                self.ui.error.setText("No es posible ingresar números negativos")

        except ValueError:
            self.ui.error.setText("Ha ingresado un dato inválido, inténtalo de nuevo")




class Est1(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.ui = Ui_est()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.ui.cerrar.clicked.connect(self.close)


class Est2(QDialog):
    def __init__(self):
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





class Est3(QDialog):
    def __init__(self):
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


class Est4(QDialog):
    def __init__(self):
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

class Est5(QDialog):
    def __init__(self):
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
class Est6(QDialog):
    def __init__(self):
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




        self.ui.Region.setAlignment(Qt.AlignCenter)
        self.ui.CuadroDesempleados.setAlignment(Qt.AlignCenter)
        self.ui.CuadroPoblacionAct.setAlignment(Qt.AlignCenter)
        self.ui.resultado.setAlignment(Qt.AlignCenter)

    def EnviarDatosDes(self):
        NombreTerritorio = self.ui.Region.text()
        NumDesempleados = self.ui.CuadroDesempleados.text()
        PoblacionAct = self.ui.CuadroPoblacionAct.text()


        try:

            TasaDesempleo=(int(NumDesempleados)/int(PoblacionAct)) * 100
            #print(round(TasaDesempleo,2))

            if NombreTerritorio=="":

                self.ui.resultado.setText("No puedes dejar vacío el nombre de la región")

            elif int(NumDesempleados)<=int(PoblacionAct) and int(NumDesempleados)>=0 and int(PoblacionAct)>=0:

                self.ui.resultado.setText("La tasa de desempleo en " + NombreTerritorio.upper() + " es de: \n % " + str(round(TasaDesempleo,2)))

            elif (int(NumDesempleados)>int(PoblacionAct)):

                self.ui.resultado.setText("El Numero de desempleados no\npuede ser mayor que la población")

            else:

                self.ui.resultado.setText("No es posible ingresar números negativos")




        except ValueError:

            self.ui.resultado.setText("Ha ingresado un dato inválido, inténtalo de nuevo")

        except ZeroDivisionError:

            self.ui.resultado.setText("No puedes introducir un\nnúmero 0 en la población activa")

class Ventana3(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_densidad()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.ui.cerrar.clicked.connect(self.close)


        self.ui.Region.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.ui.CuadroPob.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.ui.CuadroSup.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")

        self.ui.resultado.setAlignment(Qt.AlignCenter)
        self.ui.Region.setAlignment(Qt.AlignCenter)
        self.ui.CuadroPob.setAlignment(Qt.AlignCenter)
        self.ui.CuadroSup.setAlignment(Qt.AlignCenter)

        self.ui.enviar.clicked.connect(self.EnviarDatosDen)

    def EnviarDatosDen(self):

        NombreTerritorio = self.ui.Region.text()
        PoblacionTotal= self.ui.CuadroPob.text()
        Superficie= self.ui.CuadroSup.text()

        try:

            DensidadPoblacion=int(PoblacionTotal) / float(Superficie)

            if NombreTerritorio=="":

                self.ui.resultado.setText("No puedes dejar vacío el nombre de la región")

            elif int(PoblacionTotal)>0 and float(Superficie)>0:

                self.ui.resultado.setText("La densidad de población de \n " +str(NombreTerritorio.upper()) +  " es de "+ str(round(DensidadPoblacion,2)) + "\n personas por kilómetro cuadrado.")

            elif int(PoblacionTotal)<0 or float(Superficie)<0:

                self.ui.resultado.setText("No puedes llenar los datos\ncon números negativos.")

            elif int(PoblacionTotal)==0:

                self.ui.resultado.setText("No puedes llenar los espacios\ncon 0. Reinténtalo" )


        except ValueError:

            self.ui.resultado.setText("Has ingresado incorrectamente\nlos datos. Reinténtalo")

        except ZeroDivisionError:

            self.ui.resultado.setText("No puedes introducir 0 en los espacios" )

class Ventana4(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("cant_estrato.ui",self)
        self.ui.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.ui.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.cerrar.clicked.connect(self.close)

        self.Region.setAlignment(Qt.AlignCenter)
        self.est1.setAlignment(Qt.AlignCenter)
        self.est2.setAlignment(Qt.AlignCenter)
        self.est3.setAlignment(Qt.AlignCenter)
        self.est4.setAlignment(Qt.AlignCenter)
        self.est5.setAlignment(Qt.AlignCenter)
        self.est6.setAlignment(Qt.AlignCenter)

        self.error.setAlignment(Qt.AlignCenter)

        self.enviar.clicked.connect(self.CalcularPorcentaje)


    def CalcularPorcentaje(self):

        try:
            global NombreTerritorio
            global Estrato
            global Porcentaje
            global TotalEst

            NombreTerritorio = self.Region.text()
            Estrato=[]
            Porcentaje=[]


            Estrato.append(self.est1.text())
            Estrato.append(self.est2.text())
            Estrato.append(self.est3.text())
            Estrato.append(self.est4.text())
            Estrato.append(self.est5.text())
            Estrato.append(self.est6.text())

            if int(Estrato[0])<0 or int(Estrato[1])<0 or int(Estrato[2])<0 or int(Estrato[3])<0 or int(Estrato[4])<0 or int(Estrato[5])<0:


                self.error.setText("Ha ingresado un o más números negativos.\nReinténtalo")

            if NombreTerritorio=="":

                self.error.setText("No puedes dejar vacío el nombre de la región")

            else:

                if int(Estrato[0])>=0 and int(Estrato[1])>=0 and int(Estrato[2])>=0 and int(Estrato[3])>=0 and int(Estrato[4])>=0 and int(Estrato[5])>=0:
                    TotalEst=int(Estrato[0])+int(Estrato[1])+int(Estrato[2])+int(Estrato[3])+int(Estrato[4])+int(Estrato[5])

                    for i in [0,1,2,3,4,5]:
                        Porcentaje.append((100 * float(Estrato[i]))/float(TotalEst))

                    self.close()
                    ResultadoPorc = Porcentajes()
                    ResultadoPorc.exec()






        except ValueError:

            self.error.setText("Has ingresado incorrectamente\nlos datos. Reinténtalo")

        except ZeroDivisionError:

            self.error.setText("No puedes introducir 0 en los espacios" )


class Porcentajes(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("porcentajes.ui",self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.cerrar.clicked.connect(self.close)


        self.porc1.setAlignment(Qt.AlignCenter)
        self.porc2.setAlignment(Qt.AlignCenter)
        self.porc3.setAlignment(Qt.AlignCenter)
        self.porc4.setAlignment(Qt.AlignCenter)
        self.porc5.setAlignment(Qt.AlignCenter)
        self.porc6.setAlignment(Qt.AlignCenter)
        self.total.setAlignment(Qt.AlignCenter)

        self.porc1.setText("El Porcentaje del Estrato 1 en\n " + str(NombreTerritorio.upper()) + "\nes de %" + str(round(Porcentaje[0],2)))
        self.porc2.setText("El Porcentaje del Estrato 2 en\n " + str(NombreTerritorio.upper()) + "\nes de %" + str(round(Porcentaje[1],2)))
        self.porc3.setText("El Porcentaje del Estrato 3 en\n " + str(NombreTerritorio.upper()) + "\nes de %" + str(round(Porcentaje[2],2)))
        self.porc4.setText("El Porcentaje del Estrato 4 en\n " + str(NombreTerritorio.upper()) + "\nes de %" + str(round(Porcentaje[3],2)))
        self.porc5.setText("El Porcentaje del Estrato 5 en\n " + str(NombreTerritorio.upper()) + "\nes de %" + str(round(Porcentaje[4],2)))
        self.porc6.setText("El Porcentaje del Estrato 6 en\n " + str(NombreTerritorio.upper()) + "\nes de %" + str(round(Porcentaje[5],2)))

        self.total.setText("El total de viviendas en\n" + str(NombreTerritorio.upper()) + "\nes de: " + str(TotalEst) )


#Inicializa la aplicacion
app=QApplication(sys.argv)

#Crea un objeto de la clase Menu
menu=Menu()

#Muestra la ventana
menu.show()

#Ejecuta la aplicacion
app.exec()
