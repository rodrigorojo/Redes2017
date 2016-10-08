#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import sys
from Constants.Constants import *
from threading import Thread
import multiprocessing as mp

"""**************************************************
Fucnion para crear un cliente
**************************************************"""
class MyApiClient:

    """**************************************************
    Constructor de la clase
    @param <str> host: El host al cual se conectara
    @param <int> contact_port: El puerto al cual se conectara
    **************************************************"""
    def __init__(self, host = None, contact_port = None):
        self.contact_port = contact_port
        self.host = host
        if contact_port and host:
            #print "Nuevo Cliente en puerto: "+ str(contact_port)
            self.server = xmlrpclib.ServerProxy(Constants().HTTP+ host +Constants().TWO_DOTS+str(contact_port), allow_none = True)
            print "cliente en: "+Constants().HTTP+ host +Constants().TWO_DOTS+str(contact_port)
    """**************************************************
    Funcion para enviar mensajes
    @param <str> message: El mensaje que enviara
    **************************************************"""
    def client_send_message(self, mensaje):
        #print "cliente en host: "+str(self.host)+ " : "+str(self.contact_port)+"envio mensaje"
        print "El mensaje que se enviara es: " + str(mensaje)
        #interfaz.insertPlainText("YO: " + str(mensaje) +"\n")
        return self.server.recibe_mensaje(str(mensaje))

        ##print "cliente en host: "+str(self.host)+ " : "+str(self.contact_port)+"envio mensaje"
        #print "entroooooooo client"
        #interfaz.insertPlainText("YO: " + str(message) +"\n")
        #self.server.recibe_mensaje(message)
        #print "aqui ya no client"
