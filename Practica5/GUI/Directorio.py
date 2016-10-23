from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Constants.Constants import *
from Channel.ApiClient import MyApiClient
from Channel.Channel import *
from LoginWindow import *
import multiprocessing as mp
######para la llamada
from CallWindow import *
######
from VideocallWindow import *

"""**************************************************
La instancia de esta clase crea una ventana de chat con un canal
**************************************************"""
class Directorio(QtGui.QDialog):
    def __init__(self, parent=None, my_port = None,server_contactos_port = None, ip = None):
        super(Directorio, self).__init__(parent)

        self.my_port = my_port
        self.server_contactos_port = contact_port
        self.ip = ip

        self.P1 = QLabel(self)
        self.P1.setText("Lista de Contactos")
        self.muestraDirectorio = QListWidget(self)

        for i in range(20):
            self.muestraDirectorio.addItem('Contacto: %s' % (i + 1))

        self.buttonConectar = QPushButton("Conectar a contacto", self)
        self.buttonConectar.clicked.connect(self.conectar)

        layout = QVBoxLayout(self)
        layout.addWidget(self.P1)
        layout.addWidget(self.muestraDirectorio)
        layout.addWidget(self.buttonConectar)

        self.setWindowTitle("Directorio")

    def conectar(self):
        print "username" + str(self.muestraDirectorio.currentItem().text())
