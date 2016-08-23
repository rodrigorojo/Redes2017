#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import sys
from Constants.Constants import *

class MyApiClient:

    def __init__(self, host = None, contact_port = None):
        self.contact_port = contact_port
        if contact_port and host:
            #print "Nuevo Cliente en puerto: "+ str(contact_port)
            self.server = xmlrpclib.Server(Constants().HTTP+ host +Constants().TWO_DOTS+str(contact_port), allow_none = True)

    def client_send_message(self, message):
        #print "cliente en puerto "+str(self.contact_port)+"envio mensaje"
        return self.server.recive_message(str(message))
