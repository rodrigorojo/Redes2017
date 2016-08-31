from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Constants.Constants import *
from Channel.ApiClient import MyApiClient
from Channel.Channel import Channel
from LoginWindow import *
import multiprocessing as mp
from Constants.Constants import *
"""**************************************************
La instancia de esta clase crea una ventana de llamada de voz
**************************************************"""
class Call(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Call, self).__init__(parent)
        #self.mc = Channel(Constants().EMPTY_STR, int(my_port), int(contact_port))
        self.Con = QLabel(self)
        self.Con.setText(Constants().LLAMADADV)

        layout = QVBoxLayout(self)
        layout.addWidget(self.Con)
        #layout2 = QHBoxLayout(self)
        #layout.addLayout(layout2)
        self.setWindowTitle(Constants().LLAMADA)
        self.resize(300, 200)
