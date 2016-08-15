import sys
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from GUI.GUI import Login
from GUI.GUI import Calculadora

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtGui.QDialog.Accepted:
        window = Calculadora()
        window.show()
        sys.exit(app.exec_())
