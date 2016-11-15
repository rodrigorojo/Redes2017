from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Channel.Channel import RequestChannel
from Channel.ApiServer import *
from Constants.Constants import *
from RegistroWindow import *
import threading
"""**************************************************
Clase para crear una ventana de login
**************************************************"""
class Login(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.P0 = QLabel(self)
        self.P0.setText("Ingresa tu nombre de usuario")
        self.textP0 = QLineEdit(self)

        self.C1 = QLabel(self)
        self.C1.setText("Ingresa tu contrasena")
        self.textC1 = QLineEdit(self)
        self.textC1.setEchoMode(QLineEdit.Password);

        self.P1 = QLabel(self)
        self.P1.setText(INFOPORT1)
        self.textP1 = QLineEdit(self)

        self.P2 = QLabel(self)
        self.P2.setText(INFOPORT2)
        self.textP2 = QLineEdit(self)

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
        layout.addWidget(self.P2)
        layout.addWidget(self.textP2)
        layout.addWidget(self.buttonLogin)
        layout.addWidget(self.buttonRegistro)

        self.setWindowTitle(INFO)
    """**************************************************
    Funcion que usa el boton buttonLogin entrar
    **************************************************"""
    def button_login(self):
        print str(self.textP1.text())
        print self.textP0.text()
        print self.textC1.text()
        directory_client = xmlrpclib.ServerProxy("http://localhost:"+str(self.textP2.text()), allow_none = True)
        if directory_client.handleLogin(str(self.textP0.text()), str(self.textC1.text())):
            print int(str(self.textP1.text()))
            self.accept()
        else:
            msg1 = QMessageBox()
            msg1.setIcon(QMessageBox.Information)
            msg1.setText("Usuario o contrasena incorrectos")
            msg1.exec_()


    """**************************************************
    Funcion auxiliar
    **************************************************"""
    def regresa_str(self):
        tmp = []
        tmp.append((str(self.textP1.text())))
        tmp.append((str(self.textP2.text())))
        tmp.append((str(self.textP0.text())))
        return tmp
    """**************************************************
    Funcion que usa el boton buttonLogin entrar
    **************************************************"""
    def button_registro(self):
        print "presiono registrarse"
        self.registro = Registro()
        self.registro.setModal(True)
        self.registro.show()
        #self.accept()
