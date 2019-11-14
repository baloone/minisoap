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
# Implement all possible operations
# TODO niz replace args with the arguments that you need to run the function

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
                    op(args)
                    #print(str(op) + str(args))
                except Exception as e:
                    print("Error in instruction " + str(op) + "args")
            
            
    def reset(self):
        self.pipeline = Queue.Queue()
    
    
    def stop(self):
        print("STOP")
        exit(0)

    ###################################################### OPERATIONS
    
    
    ################# MAIN OPERATIONS
    def openn(self, file_path, file_id, mode):
        if (mode == "in"):
            stream = Input(file_path)
            self.stream_in.update({file_id: stream})
        elif (mode == "out"):
            stream = Output(file_path, None)
            self.stream_out.update({file_id: stream})
        print("OPEN")
        
    #def read 

    def close(self, file_id, mode):
        if (mode == "in"):
            s = self.stream_in.pop(file_id)
        elif (mode == "out"):
            s = self.stream_out.pop(file_id)
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
            fs = s.framerate()
            track = s.read(float(t)*fs)
        self.av_tracks.update({track_id: track})
        
    
            
            
            


    ################# GENERATOR OPERATIONS
    def sine(self, track_id, A, t, ):
        stream.update({track_id: g.sine_t()})
        print("SINE")
    
    def constant(self, *args):
        print("CONSTANT")
    
    def silence(self, *args):
        print("SILENCE")
        
    ################# OPERATOR ON STREAMS
    def identity(self, *args):
        print("IDENTITY")

    def nullify(self, *args):
        print("NULLIFY")

    def fade(self, *args):
        print("IDENTITY")

    def crossfade(self, *args):
        print("CROSSFADE")








