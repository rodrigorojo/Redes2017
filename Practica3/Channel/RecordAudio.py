import Queue
import pyaudio
import wave
import numpy
import multiprocessing as mp
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from Constants.Constants import *
class RecordAudio(object):
    """docstring for RecordAudio."""
    global frames
    frames = []
    def __init__(self):
        super(RecordAudio, self).__init__()

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
        print("* done recording2")

    def start_recording(self):
        queue = mp.Queue()
        p = mp.Process(target=self.feed_queue(queue))
        p.start()
        self.feed_queue(queue)

    def idk_audio(self, host = None, port = None):
        if host != None:
            self.server = xmlrpclib.ServerProxy(Constants().HTTP+ host +Constants().TWO_DOTS+Constants().DEFAULT_PORT, allow_none = True)
        else:
            self.server = xmlrpclib.ServerProxy(Constants().LOCALHOST +Constants().TWO_DOTS+str(port), allow_none = True)
        import numpy
        while True:
            d = queue.get()
            data = xmlrpclib.Binary(d)
            proxy.playAudio(data)

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
    def reproduce(self):
        while True:
            if len(frames) > 0:
                cv2.imshow('Servidor',frames.pop(0))
                if cv2.waitKey(1) & 0xFF==ord('q'):
                    break
        cv2.destroyAllWindows()
    def create_thead(self):
        self.playVThread = Thread(target=RecordAudio().reproduce())
        self.playVThread.setDaemon(True)
        self.playVThread.start()
