from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Constants.Constants import *
from Channel.ApiClient import MyApiClient
from Channel.Channel import Channel

class Chat(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Chat, self).__init__(parent)

        self.Con = QLabel(self)
        self.Con.setText(Constants().CONV)

        self.Conv = QLineEdit(self)

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
        mc = MyApiClient("localhost",8001)
        temp = self.Conv.text()
        self.Conv.setText(temp +"\n"+mc.client_send_message(str(self.restext.text())))
        self.restText.setText("")
