from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Constants.Constants import *
from Channel.ApiClient import MyApiClient
from Channel.Channel import Channel
from LoginWindow import *
import multiprocessing as mp

######para la llamada
#from CallWindow import *
from Channel.RecordAudio import *
######

"""**************************************************
La instancia de esta clase crea una ventana de chat con un canal
**************************************************"""
class Chat(QtGui.QDialog):
    def __init__(self, parent=None, my_port = None,contact_port = None, ip = None):
        super(Chat, self).__init__(parent)
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

        self.buttonCall = QPushButton("Llamar", self)
        self.buttonCall.clicked.connect(self.llamar)

        layout = QVBoxLayout(self)
        layout.addWidget(self.Con)
        layout.addWidget(self.Conv)
        layout2 = QHBoxLayout(self)
        layout2.addWidget(self.restext)
        layout2.addWidget(self.buttonres)
        layout2.addWidget(self.buttonCall)
        layout.addLayout(layout2)

        self.setWindowTitle(Constants().CHAT)

    """**************************************************
    Funcion que crea una nueva ventana de llamar
    **************************************************"""
    def llamar(self):
        self.ventanaLlamada = CallWindow(self.mc)
        self.ventanaLlamada.show()

    """**************************************************
    Funcion que usa el boton buttonres para enviar el mensaje
    **************************************************"""
    def responder(self):
        print "oprimio boton responder con texto: " + str(self.restext.text())
        self.Conv.insertPlainText("YO: " + str(self.restext.text()) +"\n")
        self.mc.client.client_send_message(self.restext.text())
        self.restext.setText(Constants().EMPTY_STR)

class CallWindow(QtGui.QDialog):
    def __init__(self, canal):
        super(CallWindow, self).__init__()
        self.mc = canal
        self.buttonStart = QPushButton("Empezar llamada", self)
        self.buttonStart.clicked.connect(self.llamar)

        self.buttonStop = QPushButton("Terminar Llamada", self)
        self.buttonStop.clicked.connect(self.colgar)

        layout = QVBoxLayout(self)
        layout2 = QHBoxLayout(self)
        layout2.addWidget(self.buttonStart)
        layout2.addWidget(self.buttonStop)
        layout.addLayout(layout2)

        self.setWindowTitle("Llamada")
        
    def llamar(self):
        print "Empezar el hilo y grabar o algo asi"
        self.mc.client.estaLlamando = True;
        self.mc.client.llamada_en_thread()

    def colgar(self):
        self.mc.client.stop_llamada();
        print "oprimio boton Terminar Llamada"
