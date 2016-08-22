from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Constants.Constants import *
from Channel.ApiClient import MyApiClient
from Channel.Channel import Channel
from LoginWindow import *

class Chat(QtGui.QDialog):
    def __init__(self, parent=None, puerto = None):
        #self.cliente = None
        #self.cliente = c.crea_cliente1(puerto);
        #self.cliente = c.crea_cliente2();
        self.puerto = puerto
        super(Chat, self).__init__(parent)
        self.Con = QLabel(self)
        self.Con.setText(Constants().CONV)

        self.Conv = QTextEdit(self)
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

    def responder(self):

        mc = MyApiClient("localhost",self.puerto)
        #self.Conv = [" "]
        print "oprimio boton responder con texto: " + str(self.restext.text())
        tmplst = mc.client_send_message(str(self.restext.text()))#)
        for elm in tmplst:
            self.Conv.append(elm)
        # = tmplst
        self.restext.setText("")
