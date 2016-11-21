from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import multiprocessing as mp
from Channel.RecordAudio import *
from Channel.ApiClient import MyApiClient

class CallWindow(QtGui.QDialog):
    def __init__(self, ip, contact_port):
        super(CallWindow, self).__init__()
        #self.mc = canal
        self.client = MyApiClient(ip, contact_port)

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
        print "Empezar el hilo y grabar"
        self.client.audio_thread()

    def colgar(self):
        self.mc.client.stop_llamada();
        #print "oprimio boton Terminar Llamada"
