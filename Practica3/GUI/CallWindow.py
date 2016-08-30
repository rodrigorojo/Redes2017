from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Constants.Constants import *
from Channel.ApiClient import MyApiClient
from Channel.Channel import Channel
from LoginWindow import *
import multiprocessing as mp
from Channel.RecordAudio import *
"""**************************************************
La instancia de esta clase crea una ventana de chat con un canal
**************************************************"""
class Call(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Call, self).__init__(parent)
        #self.mc = Channel(Constants().EMPTY_STR, int(my_port), int(contact_port))
        self.Con = QLabel(self)
        self.Con.setText("Llamada de voz...")

        layout = QVBoxLayout(self)
        layout.addWidget(self.Con)
        #layout2 = QHBoxLayout(self)
        #layout.addLayout(layout2)
        self.setWindowTitle("Llamada")
        self.resize(300, 200)
