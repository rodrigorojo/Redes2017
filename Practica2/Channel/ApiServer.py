#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import sys

class MyApiServer:
    def __init__(self, my_port = None):
        self.my_port = my_port
        self.server = SimpleXMLRPCServer(("localhost", int(my_port)), allow_none = True)
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.funtionWrapper = FunctionWrapper()
        self.server.register_instance(self.funtionWrapper)
        print "El servidor: localhost: "+ str(my_port)+" empezo"
        self.server.serve_forever()

    def start_server(self):
        #server = MyApiServer(myPort).server
        api_server_thread = Thread(target=self.server.serve_forever )
        api_server_thread.start()

class FunctionWrapper:
    def __init__(self):
        print "TODO FW"

    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        print message
        return message


def main(args):
   myPort = int(args[0])
   server = MyApiServer(myPort).server
   api_server_thread = Thread(target=server.serve_forever )
   api_server_thread.start()
if __name__ == '__main__':
   main(sys.argv[1:])
