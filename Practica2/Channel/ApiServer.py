#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import sys
from threading import Thread
from Constants.Constants import *
"""**************************************************
Clase para crear un servidor xmlrpc
**************************************************"""
class MyApiServer:
    """**************************************************
    Constructor de la clase
    @param <str> my_port: El puerto en el que se pondra el servidor
    **************************************************"""
    def __init__(self, my_port = None):
        global conversation
        conversation = []
        self.my_port = my_port
        self.server = SimpleXMLRPCServer((Constants().LOCALHOST, int(my_port)), allow_none = True)
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.functionWrapper = FunctionWrapper()
        self.server.register_instance(self.functionWrapper)
        self.server.register_function(self.recive_message, Constants().RECIVE_MESSAGE_FUNC)

    """**************************************************
    Fucnion para empezar el servidor
    **************************************************"""
    def init_server(self):
        self.server.serve_forever()
    """**************************************************
    Funcion que recive un mensaje y lo agrega a la lista de mensajes
    @param <str> msg: mensaje que recive
    **************************************************"""
    def recive_message(self, msg):
        conversation.append(msg)
        return conversation
    """**************************************************
    Fucnion auxiliar
    **************************************************"""
    def get_lst_conv(self, qline):
        for elm in conversation:
            qline.append(elm)

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
