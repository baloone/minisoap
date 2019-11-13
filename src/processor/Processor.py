#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from processor.ProcessorArch import ProcessorArch
# Implement all possible operations
# TODO niz replace args with the arguments that you need to run the function

class Processor(ProcessorArch):
    
    def __init__(self):
        super().__init__()
    
    ################# MAIN OPERATIONS
    def openn(self, *args):
        print("OPEN")

    def close(self, *args):
        print("CLOSE")


    def stop(self, *args):
        print("STOP")
        exit(0)

    ################# GENERATOR OPERATIONS
    def sine(self, *args):
        print("SINE")

    ################# OPERATOR ON STREAMS
    def identity(self, *args):
        print("IDENTITY")

    def crossfade_exp(self, *args):
        print("CROSSFADE")

    def nullify(self, *args):
        print("NULLIFY")







