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
from cStringIO import StringIO
import socket
import wave
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
        self.TCP_IP = host
        self.TCP_PORT = int(contact_port)
        self.BUFFER_SIZE = 1024
        self.estaLlamando = False
        self.estaVideollamando = False

    """**************************************************
    Funcion para enviar mensajes
    @param <str> message: El mensaje que enviara
    **************************************************"""
    def client_send_message(self, mensaje):
        print "El mensaje que se enviara es: " + str(mensaje)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.TCP_IP, self.TCP_PORT))
        self.s.send(str(mensaje))

    def audio_thread(self):
        self.thread1 = Thread(target=self.client_send_audio())
        self.thread1.daemon = True
        self.thread1.start()

    def client_send_audio(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = 100
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.TCP_IP, self.TCP_PORT))
        p = pyaudio.PyAudio()
        self.stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)
        print("*recording")

        self.thread2 = Thread(target=self.aux())
        self.thread2.daemon = True
        self.thread2.start()

    def aux(self):
        CHUNK = 1024
        RATE = 44100
        RECORD_SECONDS = 100
        frames = []
        for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
            self.data  = self.stream.read(CHUNK)
            frames.append(self.data)
            self.s.sendall(self.data)

    def client_record_audio(self):
        pass

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
            cv2.imshow(Constants().CLIENTE,self.frame)
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
