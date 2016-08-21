from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Constants.Constants import *

class Chat(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Chat, self).__init__(parent)

        self.Con = QLabel(self)
        self.Con.setText(Constants().CONV)

        self.Conv = QLineEdit(self)

        self.restext = QLineEdit(self)

        self.buttonres = QPushButton(Constants().RES, self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.Con)
        layout.addWidget(self.Conv)
        layout2 = QHBoxLayout(self)
        layout2.addWidget(self.restext)
        layout2.addWidget(self.buttonres)
        layout.addLayout(layout2)

        self.setWindowTitle(Constants().CHAT)
