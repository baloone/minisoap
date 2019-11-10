#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:49:29 2019

@author: nizar
"""
from InputStream import InputStream as Input
from OutputStream import OutputStream as Output


def IO_Test ():
    wave1 = Input("samples/sanctuary.wav")
    x = wave1.read_all()
    #wave2 = Output ("samples/ResultOfSanctuaryWithTracks.wav", x)
    #wave2.write()
    #print(x.get_raw_data()[0, 44])
    #print(x.get_header())
        
    
if __name__ == "__main__": 
    IO_Test()