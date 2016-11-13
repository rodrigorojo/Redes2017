from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Channel.Channel import RequestChannel
from Channel.ApiServer import *
from Constants.Constants import *
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

        self.P1 = QLabel(self)
        self.P1.setText(INFOPORT1)
        self.textP1 = QLineEdit(self)

        self.P2 = QLabel(self)
        self.P2.setText(INFOPORT2)
        self.textP2 = QLineEdit(self)

        self.buttonLogin = QPushButton(ACC, self)
        self.buttonLogin.clicked.connect(self.button_login)

        layout = QVBoxLayout(self)
        layout.addWidget(self.P0)
        layout.addWidget(self.textP0)
        layout.addWidget(self.P1)
        layout.addWidget(self.textP1)
        layout.addWidget(self.P2)
        layout.addWidget(self.textP2)
        layout.addWidget(self.buttonLogin)

        self.setWindowTitle(INFO)
    """**************************************************
    Funcion que usa el boton buttonLogin entrar
    **************************************************"""
    def button_login(self):
        print int(str(self.textP1.text()))
        self.accept()
        #self.regresa_str()
        #return c
    """**************************************************
    Funcion auxiliar
    **************************************************"""
    def regresa_str(self):
        tmp = []
        tmp.append((str(self.textP1.text())))
        tmp.append((str(self.textP2.text())))
        tmp.append((str(self.textP0.text())))
        return tmp
