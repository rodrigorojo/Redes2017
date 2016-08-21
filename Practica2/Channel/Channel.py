#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import ApiClient
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
    def __init__(self, contact_ip = None, contact_port = None):
        if (contact_port == 5000):
            self.client = ApiClient(str("get_ip_address"), 5000)
        else:
            self.client = ApiClient("localhost",contact_port)

        #if contact_ip is not "":
        #    self.client = ApiClient(str(contact_ip), 5000)
        #if contact_port:
        #    self.client = ApiClient("localhost",contact_port)


    """**************************************************
    Metodo que se encarga de mandar texto al contacto con
    el cual se estableció la conexion
    **************************************************"""
    def send_text(self, text):
        client.client_send_message(text);
