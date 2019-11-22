#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('../')
import queue as Queue
from Streams.InputStream import InputStream as Input
import libraries.generators as g
from Streams.OutputStream import OutputStream as Output
from processor.ProcessorArch import ProcessorArch
from Preconditions import *
from Streams.soundCard import *
import libraries.operations as op
import sounddevice as sd
from Streams.soundCard.InputStreamSoundCard import InputStream_SoundCard
from Streams.soundCard.OutputStreamSoundCard import OutputStream_SoundCard
import subprocess

# TODO: Add checks for all values that could be none
# ADD print functions

class Processor():
    
    def __init__(self):
        self.pipeline = Queue.Queue()
        
        self.stream_in = {}
        self.stream_out = {}
        self.av_tracks = {}
        
    
    
    
    ###################################################### CONTROL OPERATIONS
    def add(self, op, args):
        self.pipeline.put((op, args))
    
    
    def execute(self):
        if(self.pipeline.empty()):
            print("Pipeline empty, fill in instructions!")
        else:
            while not self.pipeline.empty():
                op, args = self.pipeline.get()
                try:
                    op(*args)
                except Exception as e:
                    print("Error in instruction " + str(op) + " " + str(args))
                    print(e)
            
            
    def reset(self):
        self.pipeline = Queue.Queue()
        self.pipeline_print = Queue.Queue()
    
    
    def stop(self):
        print("STOP")
        exit(0)

    def tracks(self):
        print(self.av_tracks)
        
    def streams(self):
        print(self.stream_in)
        
    def show(self):
        for q_item in self.pipeline.queue:
            print(q_item[0].__name__ + str(q_item[1]))
            
    def helpp():
        bashCommand = "cat help.txt" 
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
            
    ###################################################### OPERATIONS
    
    
    ################# MAIN OPERATIONS
    def openn(self, file_path, file_id):
        stream = Input(file_path)
        self.stream_in.update({file_id: stream})
        print("OPEN")
        
    
    def close(self, file_id):
        s = self.stream_in.pop(file_id)
        if (s is not None):
            s.close()
        print("CLOSE")
        
        
        
    def read(self, file_id, track_id, t="all"):
        if(t == "all"):
            s = self.stream_in.pop(file_id)
            track = s.read_all()
            s.close()
        else: 
            s = self.stream_in.get(file_id)
            fs = s.frame_rate()
            track = s.read_n_frames(int(float(t)*fs))
        self.av_tracks.update({track_id: track})
        
    
    def write(self, file_path, track_id):
        track = self.av_tracks.get(track_id)
        stream = Output(file_path, track)
        stream.write()
    
    
    def free(self, track_id):
        self.pop(track_id)
    
    
    def record(self, nchannels, framerate, device=sd.default.device):
        sd = InputStream_SoundCard(nchannels, framerate, device=device)
        self.stream_in.update({"soundcard" : sd})
        
        
    def stop_record(self, track_id, nframes):
        sd = self.stream_in.pop("soundcard")
        self.av_tracks.update({track_id : sd.read(nframes)})
        sd.close()
        
        
    def play(self, track_id, device=sd.default.device):
        track = self.av_tracks.get(track_id)
        sd = OutputStream_SoundCard(track, device=device)
        sd.write()
        self.stream_out.update({"soundcard" : sd})
        
        
    def stop_play(self):
        sd = self.stream_in.pop("soundcard")
        sd.close()
    
    ################# GENERATOR OPERATIONS
    def sine(self, track_id, A, t, f, start = 0, nchannels = 2, samplewidth =2, fs = 44100): #last four agrs are optional 
        self.av_tracks.update({track_id: g.sine_t(A, t, f, start = start, nchannels = nchannels,  samplewidth = samplewidth, fs = fs)})
        print("SINE")
    
    def constant(self, track_id, t, value, start = 0, nchannels = 2, samplewidth = 2, fs=44100):
        self.av_tracks.update({track_id: g.constant_t(t, value, start = start, nchannels = nchannels, samplewidth = samplewidth, fs=fs)})
        print("CONSTANT")
    
    def silence(self, track_id, t, start = 0, nchannels = 2, samplewidth = 2, fs=44100):
        self.constant(track_id, t, 0, start = start, nchannels = nchannels, samplewidth = samplewidth, fs=fs)
        print("SILENCE")
        
    ################# OPERATIONS ON TRACKS
    def nullify(self, track_id_in, track_id_out, start=0, end=None):
        track = self.av_tracks.get(track_id_in)
        self.av_tracks.update({track_id_out : op.nullify(track, start, end)})


        
    def fade(self, track_id_in, track_id_out, factor, t):
        track = self.av_tracks.get(track_id_in)
        self.av_tracks.update({track_id_out : op.fade_exp(track, factor, t)})

    def fadeinv(self, track_id_in, track_id_out, factor, t):
        track = self.av_tracks.get(track_id_in)
        self.av_tracks.update({track_id_out : op.fade_inv(track, factor, t)})

    def amplitude(self, track_id_in, track_id_out, a):
        track = self.av_tracks.get(track_id_in)
        self.av_tracks.update({track_id_out : op.amplitude(track, a)})


    def stereo(self, track_id_in1, track_id_in2, track_id_out):
        track1 = self.av_tracks.get(track_id_in1)
        track2 = self.av_tracks.get(track_id_in2)
        self.av_tracks.update({track_id_out : op.mono_to_stereo(track1, track2)})


    def crossfade(self, track_id_in1, track_id_in2, track_id_out, factor, t):
        track1 = self.av_tracks.get(track_id_in1)
        track2 = self.av_tracks.get(track_id_in2)
        self.av_tracks.update({track_id_out : op.crossfade_exp(track1, track2, factor, t)})




    def mix(self, track_id_in1, track_id_in2, track_id_out, t, a1=0.5, a2=0.5):
        track1 = self.av_tracks.get(track_id_in1)
        track2 = self.av_tracks.get(track_id_in2)
        self.av_tracks.update({track_id_out : op.add(track1, track2, t, a1, a2)})


    def convolve(self, track_id_in1, track_id_in2, track_id_out):
        track1 = self.av_tracks.get(track_id_in1)
        track2 = self.av_tracks.get(track_id_in2)
        self.av_tracks.update({track_id_out : op.convolve(track1, track2)})

