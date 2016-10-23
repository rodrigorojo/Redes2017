#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import sys
from Constants.Constants import *
from threading import Thread
from multiprocessing import Queue
import numpy
import pyaudio
import cv2
import time
from GUI.ChatWindow import *
from cStringIO import StringIO
"""**************************************************
Fucnion para crear un cliente
**************************************************"""
class MyApiClient():

    """**************************************************
    Constructor de la clase
    @param <str> host: El host al cual se conectara
    @param <int> contact_port: El puerto al cual se conectara
    **************************************************"""
    def __init__(self, host = None, contact_port = None):
        self.contact_port = contact_port
        self.host = host
        self.estaLlamando = False
        self.estaVideollamando = False
        if contact_port and host:
            #print "Nuevo Cliente en puerto: "+ str(contact_port)
            self.server = xmlrpclib.ServerProxy(HTTP+ host +TWO_DOTS+str(contact_port), allow_none = True)
            print "cliente en: "+HTTP+ host +TWO_DOTS+str(contact_port)
    """**************************************************
    Funcion para enviar mensajes
    @param <str> message: El mensaje que enviara
    **************************************************"""
    def client_send_message(self, mensaje):
        #print "cliente en host: "+str(self.host)+ " : "+str(self.contact_port)+"envio mensaje"
        print "El mensaje que se enviara es: " + str(mensaje)
        #interfaz.insertPlainText("YO: " + str(mensaje) +"\n")
        return self.server.recibe_mensaje(str(mensaje),self.server)

    """**************************************************
    Funcion que hace que la videollamada termine
    **************************************************"""
    def stop_videollamada(self):
        self.estaVideollamando = False
        print "La llamada termino"
    """**************************************************
    Funcion que pone la videollamada en un hilo
    **************************************************"""
    def videollamada_en_thread(self):
        self.thread1 = Thread(target=self.client_record_and_send_video())
        self.thread1.daemon = True
        self.thread1.start()
    """**************************************************
    Funcion que graba y envia el video al contacto
    **************************************************"""
    def client_record_and_send_video(self):
        print "El cliente enviara audio..."
        self.queue = Queue()
        self.thread1 = Thread(target=self.grabar_video,args=(self.queue,))
        self.thread1.daemon = True
        self.thread1.start()
    """**************************************************
    Funcion auxiliar
    **************************************************"""
    def toString(self,data):
        self.x = StringIO()
        numpy.lib.format.write_array(self.x,data)
        return self.x.getvalue()
    """**************************************************
    Funcion que graba video
    **************************************************"""
    def grabar_video(self,q):
        print"entro a grabar"
        self.cap = cv2.VideoCapture(0)
        while self.estaVideollamando:
            self.ret, self.frame = self.cap.read()
            cv2.imshow(CLIENTE,self.frame)
            self.data = xmlrpclib.Binary(self.toString(self.frame))
            self.server.recibe_video(self.data)
        self.cap.release()
        cv2.destroyAllWindows()

    """**************************************************
    Funcion que hace que la llamada termine
    **************************************************"""
    def stop_llamada(self):
        self.estaLlamando = False
        print "La llamada termino"
    """**************************************************
    Funcion que pone la llamada en un hilo
    **************************************************"""
    def llamada_en_thread(self):
        self.thread1 = Thread(target=self.client_record_and_send_audio)
        self.thread1.daemon = True
        self.thread1.start()
    """**************************************************
    Funcion que graba y envia el audio al contacto
    **************************************************"""
    def client_record_and_send_audio(self):
        print "El cliente enviara audio..."
        self.queue = Queue()
        self.thread_llamada = Thread(target=self.feed_queue, args=(self.queue,))
        self.thread_llamada.daemon = True
        self.thread_llamada.start();

        import numpy
        while self.estaLlamando:
            print self.queue.get()
            d = self.queue.get()
            self.server.recibe_audio(xmlrpclib.Binary(d))

    """**************************************************
    Funcion que va guardando el audio
    **************************************************"""
    def feed_queue(self, q):
        self.p = pyaudio.PyAudio()
        self.FORMAT = self.p.get_format_from_width(2)

        self.stream = self.p.open(format=self.FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        while self.estaLlamando:
            frame = []
            for i in range(0,int(RATE/CHUNK * RECORD_SECONDS)):
                frame.append(self.stream.read(CHUNK))
            self.data_ar = numpy.fromstring(''.join(frame),  dtype=numpy.uint8)
            q.put(self.data_ar)
