#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import sys
from threading import Thread

class MyApiServer:


    def __init__(self, my_port = None):
        global conversation
        conversation = []
        self.my_port = my_port
        self.server = SimpleXMLRPCServer(("localhost", int(my_port)), allow_none = True)
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.functionWrapper = FunctionWrapper()
        self.server.register_instance(self.functionWrapper)
        self.server.register_function(self.recive_message, "recive_message")
        print "El servidor: localhost: "+ str(my_port)+" empezo"

    def init_server(self):
        self.server.serve_forever()

    def recive_message(self, msg):
        conversation.append(msg)
        return conversation
        #for txt in conversation:
        #    print txt

    def get_lst_conv(self, qline):
        for elm in conversation:
            qline.append(elm)
            #qline = conversation
            #return qline

    def get_conv_to_string(self):
        for txt in conversation:
            conversationstr += text
            conversationstr += "\n"
        print conversationstr
        return conversationstr

class FunctionWrapper:
    def __init__(self):
        print "TODO FW"

    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        return  message

def main(args):
   myPort = int(args[0])
   server = MyApiServer(myPort).server
   api_server_thread = Thread(target=server.serve_forever )
   api_server_thread.start()
if __name__ == '__main__':
   main(sys.argv[1:])
