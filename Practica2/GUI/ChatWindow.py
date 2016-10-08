from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Constants.Constants import *
from Channel.ApiClient import MyApiClient
from Channel.Channel import Channel
from LoginWindow import *
import multiprocessing as mp

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

        layout = QVBoxLayout(self)
        layout.addWidget(self.Con)
        layout.addWidget(self.Conv)
        layout2 = QHBoxLayout(self)
        layout2.addWidget(self.restext)
        layout2.addWidget(self.buttonres)

        layout.addLayout(layout2)

        self.setWindowTitle(Constants().CHAT)

    """**************************************************
    Funcion que usa el boton buttonres para enviar el mensaje
    **************************************************"""
    def responder(self):
        print "oprimio boton responder con texto: " + str(self.restext.text())
        #self.Conv.insertPlainText("YO: " + self.restext.text()+"\n");
        self.Conv.insertPlainText("YO: " + str(self.restext.text()) +"\n")
        self.mc.client.client_send_message(self.restext.text())
        self.restext.setText(Constants().EMPTY_STR)
    """**************************************************
    Funcion auxiliar
    **************************************************"""
    def sincroniza (self, otro = None):
        #print "esta sincronizando"
        tmplst = self.mc.client.client_send_message(str(self.restext.text()))
        for elm in tmplst:
            otro.Conv.append(elm)
