# Copyright (C) 2020 Mohamed H
#
# This file is part of Minisoap.
#
# Minisoap is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Minisoap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Minisoap.  If not, see <http://www.gnu.org/licenses/>.

"""These tests works only locally
from minisoap.writer import Writer
from minisoap.generators import Silence, Sine
import time
import wave
import os
import tempfile
from functools import reduce
import numpy as np

def round(t):
    return int(1000*t+.5)/1000.0

def abctest_kill():
    tmpf = tempfile.mktemp('.wav')
    w = Writer(Silence(), tmpf)
    w.start()
    time.sleep(.05)
    w.kill()
    assert True

def test_duration():
    st = Silence(.5)
    tmpf = tempfile.mktemp('.wav')
    w = Writer(st, tmpf)
    w.start()
    while not w.killed():
        time.sleep(0.1)
    wav = wave.open(tmpf, 'r')
    d = round(wav.getnframes()/float(wav.getframerate()*wav.getsampwidth()))
    assert .5 == d

def test_channels():
    st = Silence(.5)
    tmpf = tempfile.mktemp('.wav')
    w = Writer(st, tmpf)
    w.start()
    while not w.killed():
        time.sleep(0.1)
    wav = wave.open(tmpf, 'r')
    assert wav.getnchannels() == Silence(.5).channels
def test_samplerate():

    st = Silence(.5)
    tmpf = tempfile.mktemp('.wav')
    w = Writer(st, tmpf)
    w.start()
    while not w.killed():
        time.sleep(0.1)
    wav = wave.open(tmpf, 'r')
    assert wav.getframerate()== Silence(.5).samplerate

def test__content():
    st = Silence(.5)
    tmpf = tempfile.mktemp('.wav')
    w = Writer(st, tmpf)
    w.start()
    ret = False
    while not w.killed():
        time.sleep(0.1)
    wav = wave.open(tmpf, 'r')
    for _ in range(wav.getnframes()):
        data = wav.readframes(1)
        if  data != b'\x00'*2*st.channels:
            break
    else: ret = True
    assert ret

"""
