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
from GUI.IPWindow import IPAdress
from Constants.AuxiliarFunctions import get_ip_address
from GUI.Directorio import Directorio

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
    #login.
    if local:
        login = Login()
        if login.exec_() == QtGui.QDialog.Accepted:
            lst = login.regresa_str()
            directorio = Directorio(my_username = str(lst[2]), my_port = lst[0], server_contactos_port = lst[1], ip = "localhost");
            directorio.show()
            #chat = Chat(my_port = lst[1],contact_port = lst[0])
            #chat.show()
        sys.exit(app.exec_())
    else:
        ipw = IPAdress()
        ipw.show()
        if ipw.exec_() == QtGui.QDialog.Accepted:
            lst = ipw.regresa_str()
            #print "contact_ip---->"+contact_ip
            directorio = Directorio(my_username = str(lst[0]),server_contactos_port = 5555, ip = str(lst[2]));
            directorio.show()
            #chat = Chat(ip = contact_ip)
            #chat.show()
        sys.exit(app.exec_())
    sys.exit(app.exec_())
if __name__ == '__main__':
    if(sys.argv[1:] != None):
        main(sys.argv[1:])
    else:
        main("")
