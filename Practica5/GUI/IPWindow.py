from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Channel.Channel import *
from Channel.ApiServer import *
from Constants.Constants import *
import threading
"""**************************************************
Clase para crear una ventana de login
**************************************************"""
class IPAdress(QtGui.QDialog):
    def __init__(self, parent=None):
        super(IPAdress, self).__init__(parent)

        self.P1 = QLabel(self)
        self.P1.setText("Ingresar IP")
        self.textP1 = QLineEdit(self)

        self.buttonLogin = QPushButton(ACC, self)
        self.buttonLogin.clicked.connect(self.button_login)

        layout = QVBoxLayout(self)
        layout.addWidget(self.P1)
        layout.addWidget(self.textP1)
        layout.addWidget(self.buttonLogin)


        self.setWindowTitle("Ingresar IP")
    """**************************************************
    Funcion que usa el boton buttonLogin entrar
    **************************************************"""
    def button_login(self):
        #print "el ip ingresado es: "+str(self.textP1.text()))
        self.accept()
        #return str(self.textP1.text()))

    def regresa_contact_ip(self):
        return str(self.textP1.text())
