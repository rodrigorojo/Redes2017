from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import multiprocessing as mp

class VideocallWindow(QtGui.QDialog):
    def __init__(self, cliente):
        super(VideocallWindow, self).__init__()
        self.cliente = cliente
        self.buttonStart = QPushButton("Empezar Videollamada", self)
        self.buttonStart.clicked.connect(self.llamar)

        self.buttonStop = QPushButton("Terminar Videollamada", self)
        self.buttonStop.clicked.connect(self.colgar)

        layout = QVBoxLayout(self)
        layout2 = QHBoxLayout(self)
        layout2.addWidget(self.buttonStart)
        layout2.addWidget(self.buttonStop)
        layout.addLayout(layout2)

        self.setWindowTitle("Videollamada")

    def llamar(self):
        print "Empezar el hilo y grabar"
        self.cliente.estaVideollamando = True
        #self.mc.server.leEstanVideollamando = True
        self.cliente.videollamada_en_thread()

    def colgar(self):
        self.cliente.stop_videollamada();
        #self.mc.server.leEstanVideollamando = False
        print "oprimio boton Terminar Llamada"
