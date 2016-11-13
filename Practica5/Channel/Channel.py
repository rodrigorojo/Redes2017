#! /usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################
# PURPOSE: Clase que representa la abstracción de   #
#         Un canal bidireccional, con uso de la     #
#          biblioteca xmlRpc                        #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes:                                            #
#                                                   #
# Copyright   16-08-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################

from ApiServer import *
from ApiClient import *

import xmlrpclib
from ApiServer import MyApiServer
from ApiClient import MyApiClient
from threading import Thread
from Constants.Constants import *
from Constants.AuxiliarFunctions import get_ip_address
"""**************************************************
Las instancias de esta clase contendran los metodos
necesarios para hacer uso de los metodos
del api de un contacto. Internamente Trabajara
con una proxy apuntando hacia los servicios del
servidor xmlrpc del contacto
**************************************************"""
class RequestChannel():
    """**************************************************
    Convencion: Si trabajamos de manera local, entonces
    haremos uso de los campos de contact_port y my_port
    por lo que el campo de contact_ip puede ser nulo.
    Si trabajamos con instancias en la red solo se hara uso
    del campo de contact_ip
    **************************************************"""
    """**************************************************
    Constructor de la clase
    @param <str> contact_ip: Si no se trabaja de manera local
                representa la ip del contacto con el que se
                establecera la conexion
    @param <int> my_port: De trabajar de manera local puerto
                de la instancia del cliente
    @param <int> contact_port: De trabajar de manera local
                representa el puerto de la instancia del contacto
    **************************************************"""
    def __init__(self, contact_ip = None, my_port = None,contact_port = None):
        #self.contact_ip = contact_ip
        #self.my_port = my_port
        #self.contact_port = contact_port

        if( contact_ip == "localhost"):
            self.api_client = MyApiClient(host = LOCALHOST, contact_port = contact_port)
        else:
            self.api_client = MyApiClient(host = contact_ip, contact_port = 5000)

    """**************************************************
    Metodo que se encarga de mandar texto al contacto con
    el cual se estableció la conexion
    **************************************************"""
    def send_text(self, text):
        self.api_client.client_send_message(text)
    """**************************************************
    Metodo que se encarga de mandar iniciar una conversacion
    con un nuevo contacto
    **************************************************"""
    def new_connection(self, my_ip, my_port):
        #TODO
        print ""

    """**************************************************
    Metodo que se encarga de mandar audio y video al contacto
    con el cual se estableció la conexion
    **************************************************"""
    def begin_call(self):
        self.api_client.llamada_en_thread()
    """**************************************************
    Metodos Get
    **************************************************"""
    def get_api_client(self):
        return self.api_client


class BidirectionalChannel(RequestChannel):
    def __init__(self, Qparent= None, my_ip = None,  contact_port = None,my_port = None):
        #self.contact_ip = contact_ip
        self.my_port = my_port
        #self.contact_port = contact_port

        if( my_ip == "localhost"):
            self.server = MyApiServer(my_port = self.my_port)
            self.api_server_thread = Thread(target = self.server.init_server)
            self.api_server_thread.daemon=True
            self.api_server_thread.start()

        else:
            self.server = MyApiServer(ip = get_ip_address(), my_port= 5000)
            self.api_server_thread = Thread(target = self.server.init_server)
            self.api_server_thread.daemon = True
            self.api_server_thread.start()

    """**************************************************
    Metodos Get
    **************************************************"""
    def get_api_server(self):
        return self.server
