#! /usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import sys
from Constants.Constants import *
import GUI.VideocallCameraWindow as vccw
import pyaudio
import cv2
import cv
import numpy
import cStringIO
from threading import Thread
from PyQt4.QtCore import QPoint, QTimer
from PyQt4.QtGui import QApplication, QImage, QPainter, QWidget
"""**************************************************
Clase para crear un servidor xmlrpc
**************************************************"""
class MyApiServer(QtGui.QDialog):
    """**************************************************
    Constructor de la clase
    @param <str> my_port: El puerto en el que se pondra el servidor
    **************************************************"""
    def __init__(self, ip = None, my_port = None):
        super(MyApiServer, self).__init__(None)
        self.conversacion = QTextEdit(self)
        self.my_port = my_port
        self.frames = []
        self.leEstanVideollamando = True
        if(ip == None):
            self.server = SimpleXMLRPCServer((Constants().LOCALHOST, int(my_port)), allow_none = True)
        else:
            self.server = SimpleXMLRPCServer((ip, int(my_port)), allow_none = True)
            print "servidor en ip: " +ip+" : "+ str(int(my_port))
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.functionWrapper = FunctionWrapper()
        self.server.register_instance(self.functionWrapper)
        self.server.register_function(self.recibe_mensaje, Constants().RECIBE_MENSAJE_FUNC)
        self.server.register_function(self.recibe_audio, "recibe_audio")
        self.server.register_function(self.recibe_video, "recibe_video")

    """**************************************************
    Funcion para empezar el servidor
    **************************************************"""
    def init_server(self):
        self.server.serve_forever()
    """**************************************************
    Funcion que recibe un mensaje y lo agrega a la lista de mensajes
    @param <str> msg: mensaje que recibe
    **************************************************"""
    def recibe_mensaje(self, mensaje):
        #print "recibe____mensaje: Contacto:::" + mensaje
        self.conversacion.insertPlainText("CONTACTO: " + str(mensaje) +"\n")

    """**************************************************
    Funcion que recibe el video y se lo pasa a otra
    **************************************************"""
    def recibe_video(self,data):
        print "El video se recibio en servidor "
        self.thread = Thread(target=self.reproduce_video,args=(data,))
        self.thread.daemon = True
        self.thread.start()
    """**************************************************
    Funcion que reproduce el video
    **************************************************"""
    def reproduce_video(self,data):
        self.append_frames(data)
        #print self.leEstanVideollamando
        while self.leEstanVideollamando:
            print self.leEstanVideollamando
            if len(self.frames) > 0:
                print "|"
                cv2.imshow(Constants().SERVIDOR,self.frames.pop(0))
        print self.leEstanVideollamando
        cv2.destroyAllWindows()
    """**************************************************
    Funcion auxiliar
    **************************************************"""
    def toArray(self,s):
        self.f = cStringIO.StringIO(s)
        self.arr = numpy.lib.format.read_array(self.f)
        return self.arr
    """**************************************************
    Funcion que auxiliar
    **************************************************"""
    def append_frames(self,video):
        self.frames.append(self.toArray(video.data))

    """**************************************************
    Funcion que recibe el audio y se lo pasa a otra
    **************************************************"""
    def recibe_audio(self,audio):
        print "El audio se recibio en servidor "
        self.reproduce(audio)
    """**************************************************
    Funcion que reproduce el audio recibido
    **************************************************"""
    def reproduce(self, audio):
        print "reproduciendo..."
        self.p = pyaudio.PyAudio()
        self.FORMAT = self.p.get_format_from_width(2)
        self.stream = self.p.open(format=self.FORMAT,
                        channels=1,
                        rate=44100,
                        output=True,
                        frames_per_buffer=3024)
        self.data = audio.data
        self.stream.write(self.data)
        self.stream.close()
        self.p.terminate()
    """**************************************************
    Funcion para pegar el mensaje a la interfaz
    **************************************************"""
    def chat_window(self,msg):
        self.Conv = QTextEdit(self)
        self.Conv.setReadOnly(True)
        self.Conv.append(msg)
        return self.Conv

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
