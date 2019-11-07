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
    wave2 = Output("samples/resultOfSanctuary.wav")
    wave2.write(wave1.read_all())
        
    
if __name__ == "__main__": 
    IO_Test()