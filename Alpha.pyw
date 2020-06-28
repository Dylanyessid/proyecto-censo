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
        self.setFixedSize(607, 487)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)


        #Cargar la configuracion .ui
        uic.loadUi("menu.ui",self)

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
        self.cerrar_principal.clicked.connect(CerrarPrincipal)


        self.BotonEst.clicked.connect(ConectarEst)


        self.BotonDes.clicked.connect(ConectarDes)


        self.BotonDen.clicked.connect(ConectarDen)


        self.BotonCantEst.clicked.connect(ConectarCantEst)


class Ventana1(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        uic.loadUi("estrato.ui",self)

        self.numh.setAlignment(Qt.AlignCenter)
        self.nume.setAlignment(Qt.AlignCenter)
        self.error.setAlignment(Qt.AlignCenter)


        #Botones
        self.cerrar.clicked.connect(self.close)


        self.numh.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.nume.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")

        self.enviar.clicked.connect(self.EnviarDatosEst)




    def EnviarDatosEst(self):



        NumHabitaciones = self.numh.text()
        NumElectro = self.nume.text()
        #print(int(NumHabitaciones))
        #print(int(NumElectro))


        try:
            if self.regulares.isChecked():
                Condiciones=2
            elif self.aceptables.isChecked():
                Condiciones=4
            elif self.buenas.isChecked():
                Condiciones=8
            elif self.muybuenas.isChecked():
                Condiciones=12
            elif self.excelentes.isChecked():
                Condiciones=14


            if self.conexionsi.isChecked():
                OpcionInternet=4
            elif self.conexionno.isChecked():
                OpcionInternet=0


            if self.viassi.isChecked():
                OpcionVia=4
            elif self.conexionno.isChecked():
                OpcionVia=1



            if self.garagesi.isChecked():
                OpcionGarage=5
            elif self.garageno.isChecked():
                OpcionGarage=1



            if self.ingreso1.isChecked():
                Ingreso=2
            elif self.ingreso2.isChecked():
                Ingreso=5
            elif self.ingreso3.isChecked():
                Ingreso=7
            elif self.ingreso4.isChecked():
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

                self.error.setText("No es posible ingresar números negativos")

        except ValueError:
            self.error.setText("Ha ingresado un dato inválido, inténtalo de nuevo")




class Est1(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("est.ui",self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.cerrar.clicked.connect(self.close)
        self.cerrar.setStyleSheet("background-color:white")
        self.setStyleSheet("background-color: #5ae9f2")

class Est2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("est.ui",self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.cerrar.clicked.connect(self.close)
        self.cerrar.setStyleSheet("background-color:white")
        self.setStyleSheet("background-color: #5ae9f2")

        self.titulo.setText("Estrato 2")
        self.descripcion.setText("Este es el estrato: Bajo. Las condiciones de la casa al igual que en el entorno son un poco mejores. \nEste estrato tambien pueden recibir subsidios.")





class Est3(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("est.ui",self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.cerrar.clicked.connect(self.close)
        self.cerrar.setStyleSheet("background-color:white")
        self.setStyleSheet("background-color: #5ae9f2")

        self.titulo.setText("Estrato 3")
        self.descripcion.setText("Este estrato corresponde a: Medio-bajo. Las condiciones en las que se vive son \nconsiderables. Este estrato es el más alto en el que se pueden recibir subsidios")


class Est4(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("est.ui",self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.cerrar.clicked.connect(self.close)
        self.cerrar.setStyleSheet("background-color:white")
        self.setStyleSheet("background-color: #5ae9f2")

        self.titulo.setText("Estrato 4")
        self.descripcion.setText("Este estrato corresponde a: Medio.\nUna característica de este estrato es que no puede recibir subsidios(como los más bajos)\nni tienen que pagar sobrecostos (como los más altos).")

class Est5(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("est.ui",self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.cerrar.clicked.connect(self.close)
        self.cerrar.setStyleSheet("background-color:white")
        self.setStyleSheet("background-color: #5ae9f2")

        self.titulo.setText("Estrato 5")
        self.descripcion.setText("Este estrato corresponde a: Medio-alto.\nA partir de este estrato se debe de pagar sobrecostos en los servicios\npúblicos como contribución ya que suelen tener mayores recursos económicos.")
class Est6(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("est.ui",self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.cerrar.clicked.connect(self.close)
        self.cerrar.setStyleSheet("background-color:white")
        self.setStyleSheet("background-color: #5ae9f2")

        self.titulo.setText("Estrato 6")
        self.descripcion.setText("Este estrato corresponde a: Alto. \nEs el estrato socioeconómico más alto. Poseen excelentes condiciones\ntanto de vivienda como de entorno y también paga sobrecostos en los\nservicios públicos.")

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

        self.enviar.clicked.connect(self.EnviarDatosDes)

        self.Region.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.CuadroDesempleados.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.CuadroPoblacionAct.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.resultado.setAlignment(Qt.AlignCenter)

    def EnviarDatosDes(self):
        NombreTerritorio = self.Region.text()
        NumDesempleados = self.CuadroDesempleados.text()
        PoblacionAct = self.CuadroPoblacionAct.text()


        try:

            TasaDesempleo=(int(NumDesempleados)/int(PoblacionAct)) * 100
            #print(round(TasaDesempleo,2))

            if NombreTerritorio=="":

                self.resultado.setText("No puedes dejar vacío el nombre de la región")

            elif int(NumDesempleados)<=int(PoblacionAct) and int(NumDesempleados)>0 and int(PoblacionAct)>0:

                self.resultado.setText("La tasa de desempleo en " + NombreTerritorio.upper() + " es de: \n % " + str(round(TasaDesempleo,2)))

            elif (int(NumDesempleados)>int(PoblacionAct)):

                self.resultado.setText("El Numero de desempleados no puede ser mayor que la población")

            else:

                self.resultado.setText("No es posible ingresar números negativos")




        except ValueError:

            self.resultado.setText("Ha ingresado un dato inválido, inténtalo de nuevo")

        except ZeroDivisionError:

            self.resultado.setText("No puedes introducir un número 0 en la Población Activa")

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

        self.Region.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.CuadroPob.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.CuadroSup.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.resultado.setAlignment(Qt.AlignCenter)


        self.enviar.clicked.connect(self.EnviarDatosDen)

    def EnviarDatosDen(self):

        NombreTerritorio = self.Region.text()
        PoblacionTotal= self.CuadroPob.text()
        Superficie= self.CuadroSup.text()

        try:

            DensidadPoblacion=int(PoblacionTotal) / float(Superficie)

            if NombreTerritorio=="":

                self.resultado.setText("No puedes dejar vacío el nombre de la región")

            elif int(PoblacionTotal)>0 and float(Superficie)>0:

                self.resultado.setText("La Densidad de población de \n " +str(NombreTerritorio.upper()) +  " es de "+ str(round(DensidadPoblacion,2)) + "\n personas por kilómetro cuadrado.")

            elif int(PoblacionTotal)<0 or float(Superficie)<0:

                self.resultado.setText("No puedes llenar los datos con números negativos.")

            elif int(PoblacionTotal)==0:

                self.resultado.setText("No puedes llenar los espacios con 0. Reinténtalo" )


        except ValueError:

            self.resultado.setText("Has ingresado incorrectamente los datos. Reinténtalo")

        except ZeroDivisionError:

            self.resultado.setText("No puedes introducir 0 en los espacios" )

class Ventana4(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("cant_estrato.ui",self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Botones
        self.cerrar.clicked.connect(self.close)
        self.cerrar.setStyleSheet("background-color:white")
        self.setStyleSheet("background-color: #5ae9f2")

        self.Region.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.est1.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.est2.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.est3.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.est4.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.est5.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")
        self.est6.setStyleSheet("background-color:white; border:none; border-radius: 10px 10px")

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


                    self.error.setText("Ha ingresado un o más números negativos. Reinténtalo")

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

            self.error.setText("Has ingresado incorrectamente los datos. Reinténtalo")

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
        self.cerrar.setStyleSheet("background-color:white")
        self.setStyleSheet("background-color: #5ae9f2")

        self.porc1.setAlignment(Qt.AlignCenter)
        self.porc2.setAlignment(Qt.AlignCenter)
        self.porc3.setAlignment(Qt.AlignCenter)
        self.porc4.setAlignment(Qt.AlignCenter)
        self.porc5.setAlignment(Qt.AlignCenter)
        self.porc6.setAlignment(Qt.AlignCenter)

        self.porc1.setText("El Porcentaje del Estrato 1 en " + str(NombreTerritorio.upper()) + "\n es de %" + str(round(Porcentaje[0],2)))
        self.porc2.setText("El Porcentaje del Estrato 2 en " + str(NombreTerritorio.upper()) + "\n es de %" + str(round(Porcentaje[1],2)))
        self.porc3.setText("El Porcentaje del Estrato 3 en " + str(NombreTerritorio.upper()) + "\n es de %" + str(round(Porcentaje[2],2)))
        self.porc4.setText("El Porcentaje del Estrato 4 en " + str(NombreTerritorio.upper()) + "\n es de %" + str(round(Porcentaje[3],2)))
        self.porc5.setText("El Porcentaje del Estrato 5 en " + str(NombreTerritorio.upper()) + "\n es de %" + str(round(Porcentaje[4],2)))
        self.porc6.setText("El Porcentaje del Estrato 6 en " + str(NombreTerritorio.upper()) + "\n es de %" + str(round(Porcentaje[5],2)))

        self.total.setText("El total de viviendas en " + str(NombreTerritorio.upper()) + " es de: " + str(TotalEst) )


#Inicializa la aplicacion
app=QApplication(sys.argv)

#Crea un objeto de la clase Menu
menu=Menu()

#Muestra la ventana
menu.show()

#Ejecuta la aplicacion
app.exec()
