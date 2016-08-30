import Queue
import pyaudio
import wave
import numpy

class RecordAudio(object):
    """docstring for RecordAudio."""
    def __init__(self):
        super(RecordAudio, self).__init__()
        #self.arg = arg

    def record(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = "output.wav"

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")


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
            print("* done recording1")
        print("* done recording2")
