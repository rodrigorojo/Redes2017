#! /usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import sys
from threading import Thread
from Constants.Constants import *
import pyaudio
"""**************************************************
Clase para crear un servidor xmlrpc
**************************************************"""
class MyApiServer:
    """**************************************************
    Constructor de la clase
    @param <str> my_port: El puerto en el que se pondra el servidor
    **************************************************"""
    def __init__(self, ip = None, my_port = None):
        global conversation
        conversation = []
        self.my_port = my_port
        if(ip == None):
            self.server = SimpleXMLRPCServer((Constants().LOCALHOST, int(my_port)), allow_none = True)
        else:
            self.server = SimpleXMLRPCServer((ip, int(my_port)), allow_none = True)
            print "servidor en ip: " +ip+" : "+ str(int(my_port))
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.functionWrapper = FunctionWrapper()
        self.server.register_instance(self.functionWrapper)
        self.server.register_function(self.recive_message, Constants().RECIVE_MESSAGE_FUNC)

        #self.call_thread = Thread(target = RecordAudio().playAudio())
        #self.call_thread.daemon = True
        #self.call_thread.start()

        #self.playVThread = Thread(target=RecordAudio().manda_audio())
        #self.playVThread.setDaemon(True)
        #self.playVThread.start()

    def playAudio(self, audio):
        CHUNK = 1024
        CHANNELS = 1
        RATE = 44100
        DELAY_SECONDS = 5
        p = pyaudio.PyAudio()
        FORMAT = p.get_format_from_width(2)
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)

        self.data1 = audio.data
        stream.write(data1)
        stream.close()
        p.terminate()
    """**************************************************
    Fucnion para empezar el servidor
    **************************************************"""
    def init_server(self):
        self.server.serve_forever()
    """**************************************************
    Funcion que recive un mensaje y lo agrega a la lista de mensajes
    @param <str> msg: mensaje que recive
    **************************************************"""
    def recive_message(self, msg):
        print "recive_message: " +msg
        conversation.append(msg)
        return conversation

    def chat_window(self,msg):
        self.Conv = QTextEdit(self)
        self.Conv.setReadOnly(True)
        self.Conv.append(msg)
        return self.Conv
    """**************************************************
    Fucnion auxiliar
    **************************************************"""
    def get_lst_conv(self, qline):
        for elm in conversation:
            qline.append(elm)


class FunctionWrapper:
    def __init__(self):
        print Constants().EMPTY_STR

    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        return  message
