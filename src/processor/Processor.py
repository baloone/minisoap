#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import queue as Queue
from processor.ProcessorArch import ProcessorArch
from Preconditions import *
# Implement all possible operations
# TODO niz replace args with the arguments that you need to run the function

class Processor():
    
    def __init__(self):
        self.pipeline = Queue.Queue()
        
        self.stream_in = {}
        self.stream_out = {}
    
    
    
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
    def openn(self, *args):
        print("OPEN")

    def close(self, *args):
        print("CLOSE")

    ################# GENERATOR OPERATIONS
    def sine(self, *args):
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








