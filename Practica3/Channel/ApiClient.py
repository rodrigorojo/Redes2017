#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import sys
from Constants.Constants import *
from threading import Thread
from RecordAudio import *
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
    def client_send_message(self, message):
        #print "cliente en host: "+str(self.host)+ " : "+str(self.contact_port)+"envio mensaje"
        return self.server.recive_message(str(message))

    def client_make_call(self):
        #print "idk_audio"
        #RecordAudio().idk_audio(port=8001)
        self.call_thread = Thread(target = RecordAudio().start_recording())
        self.call_thread.daemon = True
        self.call_thread.start()
        #proxy = xmlrpclib.ServerProxy(Constants().HTTP+ self.host +Constants().TWO_DOTS+str(self.contact_port),allow_none = False)
        #import numpy
        #while True:
        #    d = queue.get()
        #    data = xmlrpclib.Binary(d)
        #    proxy.playAudio(data)
