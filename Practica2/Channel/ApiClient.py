#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import sys

class MyApiClient:

    def __init__(self, host = None, contact_port = None):
        contact_port = contact_port
        if contact_port and host:
            self.server = xmlrpclib.Server('http://'+ host +':'+str(contact_port), allow_none = True)

    def client_send_message(self, message):
        try:
            self.server.sendMessage_wrapper(str(message))
        except:
            print "ERROR: Puerto incorrecto"

if __name__ == '__main__':
    c = MyApiClient("localhost",8001)
    c.client_send_message(sys.argv[1:])
