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
class Chat(QtGui.QDialog):
    def __init__(self, parent = None, cliente = None, server = None):
        super(Chat, self).__init__(parent)
        self.cliente = cliente
        self.Con = QLabel(self)
        self.Con.setText(CONV)

        self.Conv = QTextEdit(self)
        self.Conv.setReadOnly(True)

        self.restext = QLineEdit(self)

        self.buttonres = QPushButton(RES, self)
        self.buttonres.clicked.connect(self.responder)

        self.buttonCall = QPushButton("Llamada de Audio", self)
        self.buttonCall.clicked.connect(self.llamar)

        self.buttonVideocall = QPushButton("Videollamada", self)
        self.buttonVideocall.clicked.connect(self.videollamar)

        layout = QVBoxLayout(self)
        layout.addWidget(self.Con)
        layout.addWidget(self.Conv)
        layout2 = QHBoxLayout(self)
        layout2.addWidget(self.restext)
        layout2.addWidget(self.buttonres)
        layout3 = QHBoxLayout(self)
        layout3.addWidget(self.buttonCall)
        layout3.addWidget(self.buttonVideocall)
        layout.addLayout(layout3)
        layout.addLayout(layout2)

        self.setWindowTitle(CHAT)

    """**************************************************
    Funcion que crea una nueva ventana de llamar
    **************************************************"""
    def llamar(self):
        self.ventanaLlamada = CallWindow(self.cliente)
        self.ventanaLlamada.show()

    """**************************************************
    Funcion que crea una nueva ventana de videollamar
    **************************************************"""
    def videollamar(self):
        self.ventanaVideollamada = VideocallWindow(self.cliente)
        self.ventanaVideollamada.show()

    """**************************************************
    Funcion que usa el boton buttonres para enviar el mensaje
    **************************************************"""
    def responder(self):
        print "oprimio boton responder con texto: " + str(self.restext.text())
        self.Conv.insertPlainText("YO: " + str(self.restext.text()) +"\n")
        self.cliente.client_send_message(self.restext.text())
        self.restext.setText(EMPTY_STR)
