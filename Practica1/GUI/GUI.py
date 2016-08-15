from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Code.ScientificCalculator import ScientificCalculator
import os

class Login(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.Usuario = QLabel(self)
        self.Usuario.setText("Usuario")
        self.textUsr = QLineEdit(self)

        self.Password = QLabel(self)
        self.Password.setText("Password")
        self.textPas = QLineEdit(self)
        self.textPas.setEchoMode(QtGui.QLineEdit.Password)

        self.buttonLogin = QPushButton('Ingresar', self)
        self.buttonLogin.clicked.connect(self.handleLogin)

        layout = QFormLayout(self)
        layout.addRow(self.Usuario, self.textUsr)
        layout.addRow(self.Password, self.textPas)
        layout.addRow(self.buttonLogin)

        self.setWindowTitle("Login")

    def handleLogin(self):
        logs = False
        with open('../Practica1/Code/Input.txt', 'r') as f:
            data = f.readlines()
            for line in data:
                words = line.split()
                if (self.textUsr.text() == words[2] and self.textPas.text() == words[6]):
                    logs = True
        if (logs):
            self.accept()
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'NO tienes acceso al sistema')


class Calculadora(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Calculadora, self).__init__(parent)

        self.buttonNU = QtGui.QPushButton('Nuevo Usuario', self)
        self.textCalc = QLineEdit(self)
        self.button0 = QtGui.QPushButton('0', self)
        self.button0.clicked.connect(lambda: self.change("0"))
        self.button1 = QtGui.QPushButton('1', self)
        self.button1.clicked.connect(lambda: self.change("1"))
        self.button2 = QtGui.QPushButton('2', self)
        self.button2.clicked.connect(lambda: self.change("2"))
        self.button3 = QtGui.QPushButton('3', self)
        self.button3.clicked.connect(lambda: self.change("3"))
        self.button4 = QtGui.QPushButton('4', self)
        self.button4.clicked.connect(lambda: self.change("4"))
        self.button5 = QtGui.QPushButton('5', self)
        self.button5.clicked.connect(lambda: self.change("5"))
        self.button6 = QtGui.QPushButton('6', self)
        self.button6.clicked.connect(lambda: self.change("6"))
        self.button7 = QtGui.QPushButton('7', self)
        self.button7.clicked.connect(lambda: self.change("7"))
        self.button8 = QtGui.QPushButton('8', self)
        self.button8.clicked.connect(lambda: self.change("8"))
        self.button9 = QtGui.QPushButton('9', self)
        self.button9.clicked.connect(lambda: self.change("9"))
        self.buttons = QtGui.QPushButton('+', self)
        self.buttons.clicked.connect(lambda: self.change("+"))
        self.buttonr = QtGui.QPushButton('-', self)
        self.buttonr.clicked.connect(lambda: self.change("-"))
        self.buttonm = QtGui.QPushButton('*', self)
        self.buttonm.clicked.connect(lambda: self.change("*"))
        self.buttond = QtGui.QPushButton('/', self)
        self.buttond.clicked.connect(lambda: self.change("/"))
        self.buttonp = QtGui.QPushButton('.', self)
        self.buttonp.clicked.connect(lambda: self.change("."))
        self.buttoni = QtGui.QPushButton('=', self)
        self.buttoni.clicked.connect(self.calculates)
        self.buttonmod = QtGui.QPushButton('mod', self)
        self.buttonmod.clicked.connect(lambda: self.change("mod"))
        self.buttonpot = QtGui.QPushButton('^', self)
        self.buttonpot.clicked.connect(lambda: self.change("^"))
        self.buttonc = QtGui.QPushButton('C', self)
        self.buttonc.clicked.connect(lambda: self.change(""))

        layout = QFormLayout(self)
        layout.addRow(self.buttonNU)
        layout.addRow(self.textCalc)

        r0 = QHBoxLayout(self)
        r0.addWidget(self.buttonc)
        r0.addWidget(self.buttonmod)
        r0.addWidget(self.buttonpot)
        layout.addRow(r0)

        r1 = QHBoxLayout(self)
        r1.addWidget(self.button7)
        r1.addWidget(self.button8)
        r1.addWidget(self.button9)
        r1.addWidget(self.buttond)
        layout.addRow(r1)

        r2 = QHBoxLayout(self)
        r2.addWidget(self.button4)
        r2.addWidget(self.button5)
        r2.addWidget(self.button6)
        r2.addWidget(self.buttonm)
        layout.addRow(r2)

        r3 = QHBoxLayout(self)
        r3.addWidget(self.button1)
        r3.addWidget(self.button2)
        r3.addWidget(self.button3)
        r3.addWidget(self.buttonr)
        layout.addRow(r3)

        r4 = QHBoxLayout(self)
        r4.addWidget(self.button0)
        r4.addWidget(self.buttonp)
        r4.addWidget(self.buttoni)
        r4.addWidget(self.buttons)
        layout.addRow(r4)

        self.setWindowTitle("Calculadora")

    def calculates(self):
        x = self.textCalc.text()
        c = ScientificCalculator(x)
        self.textCalc.setText(str(c.scientific_calculate()))

    def change(self, str1):
        if(str1 == ""):
            tmp = self.textCalc.text()
            self.textCalc.setText("")
        else:
            tmp = self.textCalc.text()
            self.textCalc.setText(tmp+str1)
