#! /usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import sys
from threading import Thread
from Constants.Constants import *
import pyaudio
"""**************************************************
Clase para crear un servidor xmlrpc
**************************************************"""
class MyApiServer(QtGui.QDialog):
    """**************************************************
    Constructor de la clase
    @param <str> my_port: El puerto en el que se pondra el servidor
    **************************************************"""
    def __init__(self, ip = None, my_port = None):
        super(MyApiServer, self).__init__(None)
        self.conversacion = QTextEdit(self)
        self.my_port = my_port
        if(ip == None):
            self.server = SimpleXMLRPCServer((Constants().LOCALHOST, int(my_port)), allow_none = True)
        else:
            self.server = SimpleXMLRPCServer((ip, int(my_port)), allow_none = True)
            print "servidor en ip: " +ip+" : "+ str(int(my_port))
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.functionWrapper = FunctionWrapper()
        self.server.register_instance(self.functionWrapper)
        self.server.register_function(self.recibe_mensaje, Constants().RECIBE_MENSAJE_FUNC)

    """**************************************************
    Fucnion para empezar el servidor
    **************************************************"""
    def init_server(self):
        self.server.serve_forever()
    """**************************************************
    Funcion que recibe un mensaje y lo agrega a la lista de mensajes
    @param <str> msg: mensaje que recive
    **************************************************"""
    def recibe_mensaje(self, mensaje):
        print "recibe____mensaje: Contacto:::" + mensaje
        self.conversacion.insertPlainText("CONTACTO: " + str(mensaje) +"\n")

    def chat_window(self,msg):
        self.Conv = QTextEdit(self)
        self.Conv.setReadOnly(True)
        self.Conv.append(msg)
        return self.Conv


class FunctionWrapper:
    def __init__(self):
        print Constants().EMPTY_STR

    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        return  message
