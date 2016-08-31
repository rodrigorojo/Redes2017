#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import sys
from Constants.Constants import *
from threading import Thread
import multiprocessing as mp
import pyaudio
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

        self.queue = mp.Queue()

        print "llego1"
        self.call_queue = Thread(target = self.feed_queue(self.queue))
        self.call_queue.daemon = True
        self.call_queue.start()

        print "llego2"
        self.call_send_audio = Thread(target = self.send_audio(self.queue))
        self.call_send_audio.daemon = True
        self.call_send_audio.start()

        print "llego3"

    def feed_queue(self,q):
        CHUNK = 1024
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = 2
        p = pyaudio.PyAudio()
        FORMAT = p.get_format_from_width(2)

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        print("--------------Start recording--------------")
        while True:
            print("Recording...")
            frame = []
            for i in range(0,int(RATE/CHUNK *RECORD_SECONDS)):
                frame.append(stream.read(CHUNK))
            data_ar = numpy.fromstring(''.join(frame),  dtype=numpy.uint8)
            q.put(data_ar)
            #print("* done recording1")
        print("Done recording")

    def send_audio(self, queue):
        import numpy
        while True:
            d = queue.get()
            data = xmlrpclib.Binary(d)
            self.server.playAudio(data)
