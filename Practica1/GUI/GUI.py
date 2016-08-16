from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Code.ScientificCalculator import ScientificCalculator
from Constants.Constants import *
import os

class Login(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.Usuario = QLabel(self)
        self.Usuario.setText(Constants().USUARIO)
        self.textUsr = QLineEdit(self)

        self.Password = QLabel(self)
        self.Password.setText(Constants().PASSWORD)
        self.textPas = QLineEdit(self)
        self.textPas.setEchoMode(QtGui.QLineEdit.Password)

        self.buttonLogin = QPushButton(Constants().INGRESAR, self)
        self.buttonLogin.clicked.connect(self.handleLogin)

        layout = QFormLayout(self)
        layout.addRow(self.Usuario, self.textUsr)
        layout.addRow(self.Password, self.textPas)
        layout.addRow(self.buttonLogin)

        self.setWindowTitle(Constants().LOGIN)

    def handleLogin(self):
        logs = False
        with open(Constants().PATH_DB, Constants().MODE_R) as f:
            data = f.readlines()
            for line in data:
                words = line.split()
                if (self.textUsr.text() == words[2] and self.str_to_ascii(self.textPas.text()) == words[6]):
                    logs = True
        if (logs):
            self.accept()
        else:
            QtGui.QMessageBox.warning(self, Constants().ERROR, Constants().DENIED_ACCESS)

    def str_to_ascii(self, cad):
        resultado = ""
        for c in cad:
            resultado += str(ord(str(c)))
        return resultado


class Calculadora(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Calculadora, self).__init__(parent)

        self.buttonNU = QtGui.QPushButton(Constants().NEW_USER, self)
        self.buttonNU.clicked.connect(self.agrusr)
        self.textCalc = QLineEdit(self)
        self.button0 = QtGui.QPushButton(Constants().CERO, self)
        self.button0.clicked.connect(lambda: self.change(Constants().CERO))
        self.button1 = QtGui.QPushButton(Constants().ONE, self)
        self.button1.clicked.connect(lambda: self.change(Constants().ONE))
        self.button2 = QtGui.QPushButton(Constants().TWO, self)
        self.button2.clicked.connect(lambda: self.change(Constants().TWO))
        self.button3 = QtGui.QPushButton(Constants().THREE, self)
        self.button3.clicked.connect(lambda: self.change(Constants().THREE))
        self.button4 = QtGui.QPushButton(Constants().FOUR, self)
        self.button4.clicked.connect(lambda: self.change(Constants().FOUR))
        self.button5 = QtGui.QPushButton(Constants().FIVE, self)
        self.button5.clicked.connect(lambda: self.change(Constants().FIVE))
        self.button6 = QtGui.QPushButton(Constants().SIX, self)
        self.button6.clicked.connect(lambda: self.change(Constants().SIX))
        self.button7 = QtGui.QPushButton(Constants().SEVEN, self)
        self.button7.clicked.connect(lambda: self.change(Constants().SEVEN))
        self.button8 = QtGui.QPushButton(Constants().EIGHT, self)
        self.button8.clicked.connect(lambda: self.change(Constants().EIGHT))
        self.button9 = QtGui.QPushButton(Constants().NINE, self)
        self.button9.clicked.connect(lambda: self.change(Constants().NINE))
        self.buttons = QtGui.QPushButton(Constants().ADD_SYMBOL, self)
        self.buttons.clicked.connect(lambda: self.change(Constants().ADD_SYMBOL))
        self.buttonr = QtGui.QPushButton(Constants().SUB_SYMBOL, self)
        self.buttonr.clicked.connect(lambda: self.change(Constants().SUB_SYMBOL))
        self.buttonm = QtGui.QPushButton(Constants().MULT_SYMBOL, self)
        self.buttonm.clicked.connect(lambda: self.change(Constants().MULT_SYMBOL))
        self.buttond = QtGui.QPushButton(Constants().DIV_SYMBOL, self)
        self.buttond.clicked.connect(lambda: self.change(Constants().DIV_SYMBOL))
        self.buttonp = QtGui.QPushButton(Constants().DOT, self)
        self.buttonp.clicked.connect(lambda: self.change(Constants().DOT))
        self.buttoni = QtGui.QPushButton(Constants().EQUAL, self)
        self.buttoni.clicked.connect(self.calculates)
        self.buttonmod = QtGui.QPushButton(Constants().MOD_SYMBOL, self)
        self.buttonmod.clicked.connect(lambda: self.change(Constants().MOD_SYMBOL))
        self.buttonpot = QtGui.QPushButton(Constants().POW_SYMBOL, self)
        self.buttonpot.clicked.connect(lambda: self.change(Constants().POW_SYMBOL))
        self.buttonc = QtGui.QPushButton(Constants().CLEAR, self)
        self.buttonc.clicked.connect(lambda: self.change(Constants().BLANK))

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

        self.setWindowTitle(Constants().CALCULADORA)

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

    def agrusr(self):
            self.accept()

class AgregarUsr(QtGui.QDialog):
    def __init__(self, parent=None):
        super(AgregarUsr, self).__init__(parent)

        self.Usuario = QLabel(self)
        self.Usuario.setText(Constants().USUARIO)
        self.textUsr = QLineEdit(self)

        self.Password = QLabel(self)
        self.Password.setText(Constants().PASSWORD)
        self.textPas = QLineEdit(self)
        self.textPas.setEchoMode(QtGui.QLineEdit.Password)

        self.buttonLogin = QPushButton(Constants().NEW_USER, self)
        self.buttonLogin.clicked.connect(self.handleagrusr)

        layout = QFormLayout(self)
        layout.addRow(self.Usuario, self.textUsr)
        layout.addRow(self.Password, self.textPas)
        layout.addRow(self.buttonLogin)

        self.setWindowTitle(Constants().NEW_USER)

    def handleagrusr(self):
        l = Login()
        f = open(Constants().PATH_DB,Constants().MODE_A)
        f.write(Constants().USERNAME_DB + self.textUsr.text() + Constants().PASSWORD_DB + l.str_to_ascii(self.textPas.text()) + '\n')
        f.close()
