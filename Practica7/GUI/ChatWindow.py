from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Constants.Constants import *
from Channel.ApiClient import MyApiClient
from Channel.Channel import Channel
from LoginWindow import *
import multiprocessing as mp

######para la llamada
from CallWindow import *
from Channel.RecordAudio import *
######
from VideocallWindow import *

"""**************************************************
La instancia de esta clase crea una ventana de chat con un canal
**************************************************"""
class Chat(QtGui.QDialog):
    def __init__(self, parent=None, my_port = None,contact_port = None, ip = None):
        super(Chat, self).__init__(parent)
        self.puerto_contacto = contact_port
        self.ip = ip
        if ip == None:
            self.mc = Channel(my_port = int(my_port),contact_port = int(contact_port))
        else:
            self.mc = Channel(ip, 5000, 5000)
        self.Con = QLabel(self)
        self.Con.setText(Constants().CONV)

        self.Conv = self.mc.server.conversacion
        self.Conv.setReadOnly(True)

        self.restext = QLineEdit(self)

        self.buttonres = QPushButton(Constants().RES, self)
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

        self.setWindowTitle(Constants().CHAT)

    """**************************************************
    Funcion que crea una nueva ventana de llamar
    **************************************************"""
    def llamar(self):
        self.mc.server.esTexto = False
        print "esTexto <- ", self.mc.server.esTexto
        if self.ip == None:
            self.ventanaLlamada = CallWindow(Constants().LOCALHOST,contact_port = self.puerto_contacto)
        else:
            self.ventanaLlamada = CallWindow(ip = self.ip, contact_port = self.puerto_contacto)
        self.ventanaLlamada.show()

    """**************************************************
    Funcion que crea una nueva ventana de videollamar
    **************************************************"""
    def videollamar(self):
        self.ventanaVideollamada = VideocallWindow(self.mc)
        self.ventanaVideollamada.show()

    """**************************************************
    Funcion que usa el boton buttonres para enviar el mensaje
    **************************************************"""
    def responder(self):
        self.mc.server.esTexto = True
        print "oprimio boton responder con texto: " + str(self.restext.text())
        self.Conv.insertPlainText("YO: " + str(self.restext.text()) +"\n")
        if self.ip == None:
            self.client = MyApiClient(Constants().LOCALHOST, contact_port = self.puerto_contacto)
        else:
            self.client = MyApiClient(self.ip, contact_port = self.puerto_contacto)
        self.client.client_send_message(self.restext.text())
        #self.mc.client.client_send_message(self.restext.text())
        self.restext.setText(Constants().EMPTY_STR)
