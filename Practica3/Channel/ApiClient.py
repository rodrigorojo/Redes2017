#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import sys
from Constants.Constants import *
from threading import Thread
from multiprocessing import Queue
import numpy
import pyaudio
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

    """**************************************************
    Funcion que hace que la llamada pare
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
    Funcion que graba y encia el audio al contacto
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
    Funcion que va guradando el audio
    **************************************************"""
    def feed_queue(self, q):
        self.p = pyaudio.PyAudio()
        self.FORMAT = self.p.get_format_from_width(2)

        self.stream = self.p.open(format=self.FORMAT,
                        channels=Constants().CHANNELS,
                        rate=Constants().RATE,
                        input=True,
                        frames_per_buffer=Constants().CHUNK)
        while self.estaLlamando:
            frame = []
            for i in range(0,int(Constants().RATE/Constants().CHUNK * Constants().RECORD_SECONDS)):
                frame.append(self.stream.read(Constants().CHUNK))
            self.data_ar = numpy.fromstring(''.join(frame),  dtype=numpy.uint8)
            q.put(self.data_ar)
