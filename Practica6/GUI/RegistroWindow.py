from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Channel.Channel import RequestChannel
from Channel.ApiServer import *
from Constants.Constants import *
import threading
import os
import multiprocessing as mp
from Constants.Constants import *
"""**************************************************
Clase para crear una ventana de registro
**************************************************"""
class Registro(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Registro, self).__init__(parent)
        self.P0 = QLabel(self)
        self.P0.setText("Ingresa tu nombre de usuario")
        self.textP0 = QLineEdit(self)

        self.P1 = QLabel(self)
        self.P1.setText("Ingresa tu contrasena")
        self.textP1 = QLineEdit(self)
        self.textP1.setEchoMode(QLineEdit.Password);

        self.P2 = QLabel(self)
        self.P2.setText("Vuelve a ingresar tu contrasena")
        self.textP2 = QLineEdit(self)
        self.textP2.setEchoMode(QLineEdit.Password);

        self.portLab = QLabel(self)
        self.portLab.setText("Puerto")
        self.port = QLineEdit(self)

        self.ipLab = QLabel(self)
        self.ipLab.setText("Si es remoto ingresa la ip del Servidor de Contactos")
        self.ip = QLineEdit(self)

        self.buttonRegistro = QPushButton("Registrarse",self)
        self.buttonRegistro.clicked.connect(self.button_registro)

        layout = QVBoxLayout(self)
        layout.addWidget(self.P0)
        layout.addWidget(self.textP0)
        layout.addWidget(self.P1)
        layout.addWidget(self.textP1)
        layout.addWidget(self.P2)
        layout.addWidget(self.textP2)
        layout.addWidget(self.portLab)
        layout.addWidget(self.port)
        layout.addWidget(self.ipLab)
        layout.addWidget(self.ip)
        layout.addWidget(self.buttonRegistro)

        self.setWindowTitle("Registro")

    def button_registro(self):
        if(self.textP1.text() != self.textP2.text()):
            print "no son iguales"
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ERROR")
            msg.setInformativeText("Las Contrasenas no coinciden")
            msg.setWindowTitle("Error")
            msg.setDetailedText("Errores: Las contrasenas no coinciden \nPor favor intentalo nuevamente")
            msg.exec_()
        if(self.ip.text()):
            print "es remoto"
            directory_client = xmlrpclib.ServerProxy(HTTP+ ip +TWO_DOTS+str(self.port.text()), allow_none = True)
        else:
            print "es local"
            directory_client = xmlrpclib.ServerProxy(HTTP+ "localhost" +TWO_DOTS+str(self.port.text()), allow_none = True)
            if directory_client.registra(str(self.textP0.text()), str(self.textP1.text())):
                msg1 = QMessageBox()
                msg1.setIcon(QMessageBox.Information)
                msg1.setText("Se registro Ususario")
                msg1.exec_()
            else:
                msg2 = QMessageBox()
                msg2.setIcon(QMessageBox.Information)
                msg2.setText("Ya existe el usuario")
                msg2.exec_()    
        print "hola"
