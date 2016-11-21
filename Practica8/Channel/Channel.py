#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import ApiClient
import ApiServer
from ApiServer import MyApiServer
from ApiClient import MyApiClient
from threading import Thread
from Constants.Constants import *
from Constants.AuxiliarFunctions import get_ip_address
#import AuxiliarFunctions
#from Constants.AuxiliarFunctions import AuxiliarFunctions

"""**************************************************
Las instancias de esta clase contendran los metodos
necesarios para hacer uso de los metodos
del api de un contacto. Internamente Trabajara
con una proxy apuntando hacia los servicios del
servidor xmlrpc del contacto
**************************************************"""
class Channel:
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
        self.my_port = my_port
        self.contact_port = contact_port
        print 'contact_port: ',self.contact_port,' my_port: ', self.my_port

        if( contact_ip == None):
            self.server = MyApiServer(my_port = self.my_port)
            api_server_thread = Thread(target = self.server.run_servidor)
            api_server_thread.daemon=True
            api_server_thread.start()
        else:
            self.server = MyApiServer(ip = get_ip_address(), my_port= 5000)
            api_server_thread = Thread(target = self.server.run_servidor)
            api_server_thread.daemon=True
            api_server_thread.start()
