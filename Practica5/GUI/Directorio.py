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
from ChatWindow import *
######
from VideocallWindow import *

"""**************************************************
La instancia de esta clase crea una ventana de chat con un canal
**************************************************"""
class Directorio(QtGui.QDialog):
    def __init__(self, parent=None,my_username = None ,my_port = None,server_contactos_port = None, ip = None):
        super(Directorio, self).__init__(parent)
        #remoto
        #self.directory_client = xmlrpclib.ServerProxy(HTTP+ ip +TWO_DOTS+str(server_contactos_port), allow_none = True)
        #print HTTP+ LOCALHOST +TWO_DOTS+str(server_contactos_port)
        self.adios = False
        self.my_port = my_port
        self.username = my_username
        self.directory_client = xmlrpclib.ServerProxy(HTTP+ ip +TWO_DOTS+str(server_contactos_port), allow_none = True)
        #agrega al que se conecta
        self.directory_client.connect_wrapper(LOCALHOST,str(my_port),my_username)

        #self.contacts = self.directory_client.get_contacts_wrapper(my_username)

        self.actualizar = QPushButton("Actualizar Contactos", self)
        self.actualizar.clicked.connect(self.actualizar_contactos)
        self.P1 = QLabel(self)
        self.P1.setText("Selecciona al contacto con el que \nte quieres comunicar")
        self.muestraDirectorio = QListWidget(self)
        self.actualizar_contactos()
        self.buttonConectar = QPushButton("Conectar a contacto", self)
        self.buttonConectar.clicked.connect(self.conectar)
        self.cerrar_sesion = QPushButton("Cerrar Sesion", self)
        self.cerrar_sesion.clicked.connect(self.desconectar_contacto)
        layout = QVBoxLayout(self)
        layout.addWidget(self.actualizar)
        layout.addWidget(self.cerrar_sesion)
        layout.addWidget(self.P1)
        layout.addWidget(self.muestraDirectorio)
        layout.addWidget(self.buttonConectar)

        self.setWindowTitle("Directorio")

    def conectar(self):
        username_contacto = str(self.muestraDirectorio.currentItem().text())
        print "username" + username_contacto
        dic = self.directory_client.get_contacts_wrapper(self.username)
        dic1 = dic[username_contacto]
        print dic1['NAME_CONTACT']
        print dic1['IP_CONTACT']
        print dic1['PORT_CONTACT']
        self.chat = Chat(my_port = self.my_port,contact_port = dic1['PORT_CONTACT'])
        self.chat.show()

    def actualizar_contactos(self):
        if(not self.adios):
            self.muestraDirectorio.clear()
            for key in self.directory_client.get_contacts_wrapper(self.username).keys():
                self.muestraDirectorio.addItem(str(key))

    def desconectar_contacto(self):
        self.adios = True
        self.directory_client.disconnect_wrapper_username(str(self.username))
        self.muestraDirectorio.clear()
        self.muestraDirectorio.addItem('Cerraste la Sesion')
