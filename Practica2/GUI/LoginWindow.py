from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Channel.Channel import Channel
from Channel.ApiServer import *
from Constants.Constants import *
import threading

class Login(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.P1 = QLabel(self)
        self.P1.setText(Constants().INFOPORT1)
        self.textP1 = QLineEdit(self)

        self.P2 = QLabel(self)
        self.P2.setText(Constants().INFOPORT2)
        self.textP2 = QLineEdit(self)

        self.buttonLogin = QPushButton(Constants().ACC, self)
        self.buttonLogin.clicked.connect(self.button_login)

        layout = QVBoxLayout(self)
        layout.addWidget(self.P1)
        layout.addWidget(self.textP1)
        layout.addWidget(self.P2)
        layout.addWidget(self.textP2)
        layout.addWidget(self.buttonLogin)

        self.setWindowTitle(Constants().INFO)

    def button_login(self):
        print int(str(self.textP1.text()))
        c = Channel("",int(str(self.textP1.text())),int(str(self.textP2.text())))
        self.accept()
        self.regresa_str()
        return c

    def regresa_str(self):
        tmp = []
        tmp.append((str(self.textP1.text())))
        tmp.append((str(self.textP2.text())))
        return tmp
