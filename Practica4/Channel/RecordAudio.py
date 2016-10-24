import pyaudio
import wave
import multiprocessing as mp
import time
import xmlrpclib
import numpy
import threading
from Constants.Constants import *

class RecordAudio():
    CHUNK = 1024
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 2

    
