#! /usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
# PURPOSE:Interfaz grafica de un cliente en PyQt4    #
#                                                    #
# Vilchis Dominguez Miguel Alonso                    #
#       <mvilchis@ciencias.unam.mx>                  #
#                                                    #
# Notes: El alumno tiene que implementar la parte    #
#       comentada como TODO(Instalar python-qt)      #
#                                                    #
# Copyright   16-08-2015                             #
#                                                    #
# Distributed under terms of the MIT license.        #
#################################################### #
import sys, getopt
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from GUI.LoginWindow import Login
from GUI.ChatWindow import Chat

# **************************************************
#  Definicion de la funcion principal
#**************************************************
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "l", ["local="])
    except getopt.GetoptError:
        print "#TODO lanzar exepcion"
        #TODO lanzar exepcion
    if opts: #Si el usuario mandó alguna bandera
        local = True if '-l' in opts[0] else False
    else:
        local = False
    app = QApplication(sys.argv)
    #app = QtGui.QApplication(sys.argv)
    login = Login()
    #login.

    if login.exec_() == QtGui.QDialog.Accepted:
        lst = login.regresa_str()
        print "esto es el 1------"
        print lst[0]
        chat = Chat(puerto = lst[0])
        chat.show()
        print "esto es el 2------"
        print lst[1]
        chat2 = Chat(puerto = lst[1])
        chat2.show()
    #TODO Llamar a su ventana de login
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv[1:])
