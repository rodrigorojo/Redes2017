from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Channel.Channel import *
from Channel.ApiServer import *
from Constants.Constants import *
import Constants.AuxiliarFunctions as auxfunc
import threading
from RegistroWindow import *
"""**************************************************
Clase para crear una ventana de login
**************************************************"""
class IPAdress(QtGui.QDialog):
    def __init__(self, parent=None):
        super(IPAdress, self).__init__(parent)
        print auxfunc.get_ip_address()

        self.P0 = QLabel(self)
        self.P0.setText("Ingresa tu nombre de usuario")
        self.textP0 = QLineEdit(self)

        self.C1 = QLabel(self)
        self.C1.setText("Ingresa tu contrasena")
        self.textC1 = QLineEdit(self)
        self.textC1.setEchoMode(QLineEdit.Password);

        self.P1 = QLabel(self)
        self.P1.setText("Ingresar IP del Servidor de Contactos")
        self.textP1 = QLineEdit(self)

        self.buttonLogin = QPushButton(ACC, self)
        self.buttonLogin.clicked.connect(self.button_login)

        self.buttonRegistro = QPushButton("Registrarse",self)
        self.buttonRegistro.clicked.connect(self.button_registro)

        layout = QVBoxLayout(self)
        layout.addWidget(self.P0)
        layout.addWidget(self.textP0)
        layout.addWidget(self.C1)
        layout.addWidget(self.textC1)
        layout.addWidget(self.P1)
        layout.addWidget(self.textP1)
        layout.addWidget(self.buttonLogin)
        layout.addWidget(self.buttonRegistro)


        self.setWindowTitle("Ingresar IP")
    """**************************************************
    Funcion que usa el boton buttonLogin entrar
    **************************************************"""
    def button_login(self):
        print HTTP+ str(self.textP1.text()) +TWO_DOTS+"5555"
        directory_client = xmlrpclib.ServerProxy(HTTP+ str(self.P1.text()) +TWO_DOTS+"5555", allow_none = True)
        print str(self.textP0.text())
        print str(self.textC1.text())
        if True:
            #print int(str(self.textP1.text()))
            self.accept()
        else:
            msg1 = QMessageBox()
            msg1.setIcon(QMessageBox.Information)
            msg1.setText("Usuario o contrasena incorrectos")
            msg1.exec_()


    def regresa_contact_ip(self):
        return str(self.textP1.text())

    def regresa_str(self):
        tmp = []
        tmp.append(str(self.textP0.text()))
        tmp.append(str(self.textC1.text()))
        tmp.append(str(self.textP1.text()))
        return tmp

    def button_registro(self):
        print "presiono registrarse"
        self.registro = Registro()
        self.registro.setModal(True)
        self.registro.show()
        #self.accept()
