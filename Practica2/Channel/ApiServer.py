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
        #self.conversationstr = ""
        self.my_port = my_port
        self.server = SimpleXMLRPCServer(("localhost", int(my_port)), allow_none = True)
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.functionWrapper = FunctionWrapper()
        self.server.register_instance(self.functionWrapper)
        self.server.register_function(self.add_to_conversation, "add_to_conversation")
        print "El servidor: localhost: "+ str(my_port)+" empezo"
        #self.server.serve_forever()
        api_server_thread = Thread(target=self.server.serve_forever )
        api_server_thread.start()

    def add_to_conversation(self, msg):
        conversation.append(msg)
        return conversation
        #for txt in conversation:
        #    print txt

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
        #print conversation + message
        #return message
        #new_conv = conv + "\n" + message
        #conv = new_conv
        #print conv
        #return conv


def main(args):
   myPort = int(args[0])
   server = MyApiServer(myPort).server
   api_server_thread = Thread(target=server.serve_forever )
   api_server_thread.start()
if __name__ == '__main__':
   main(sys.argv[1:])
