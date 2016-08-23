#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import ApiClient
import ApiServer
from ApiServer import MyApiServer
from ApiClient import MyApiClient
from threading import Thread
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
        self.contact_ip = contact_ip
        self.my_port = my_port
        self.contact_port = contact_port
        self.ser = MyApiServer(self.my_port)
        self.serv = MyApiServer(self.contact_port)

    def crea_cliente1(self):
        self.cliente1 = MyApiClient("localhost",self.my_port)

    def crea_cliente2(self):
        self.cliente2 = MyApiClient("localhost",self.contact_port)

    """**************************************************
    Metodo que se encarga de mandar texto al contacto con
    el cual se estableció la conexion
    **************************************************"""
    def send_text(self, text):
        return c.client_send_message(text);

if __name__ == '__main__':
    c = Channel("",8001,8001)
    print c.send_text("hola")
    c.send_text("hola")
