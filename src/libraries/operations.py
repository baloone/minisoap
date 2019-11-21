#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:22:14 2019

@author: chris
"""
import sys
sys.path.append('../')
from Streams.Tracks import Track
import numpy as np
import Preconditions as p


def nullify(track, start=0, end=None):
    if (end is None):
        return amplitude(track, 0)
    else:
        return Track(np.concatenate((track.get_data_slice(0, start), track.get_data_slice(start, end)*0, track.get_data_slice(end, track.get_time()))), track.get_size(), track.get_nchannels(), track.get_samplewidth(), track.get_framerate())


def amplitude(track, a):
    return Track(0*track.get_data(), track.get_size(), track.get_nchannels(), track.get_samplewidth(), track.get_framerate())


def convolve(track, track2):
    p.check_same_params(track, track2)
    return Track(np.convolve(track.get_data(), track2.get_data()), track.get_size(), track.get_nchannels(), track.get_samplewidth(), track.get_framerate())


def add(track, track2, t, a1=0.5, a2=0.5):
    p.check_same_params(track, track2)
    r = t*track2.get_framerate()
    extention_frames_b = track2.get_size() - r
    extention_frames_f = track.get_size() - r
    return Track(a1*track.extend_with_zeroes_behind(extention_frames_b) + a2*track2.extend_with_zeroes_front(extention_frames_f), extention_frames_b + extention_frames_f + r, track.get_nchannels(), track.get_samplewidth(), track.get_framerate())


def mono_to_stereo(track, track2):
    p.check(track.get_nchannels() == 1 and track2.get_nchannels() == 1, details ="non mono Tracks")
    p.check_same_params(track, track2)
    return Track(np.column_stack((track.get_data(), track2.get_data())), track.get_size(), 2, track.get_samplewidth(), track.get_framerate())


def fade_exp(track, factor, t):
    d = track.get_data_slice(t, track.get_size()/track.get_framerate())
    return Track(np.concatenate((track.get_data_slice(0, t), np.array([d[k, ]*2**(-factor*(k)) for k in range(np.shape(d)[0])]))), track.get_size(), track.get_nchannels(), track.get_samplewidth(), track.get_framerate()) 


def fade_inv(track, factor, t):
    d = track.get_data_slice(0, t)
    return Track(np.concatenate((d * np.array([d[k, ]*(1-2**(-factor*(k))) for k in range(np.shape(d)[0])]), track.get_data_slice(t, track.get_size()/track.get_framerate()))), track.get_size(), track.get_nchannels(), track.get_samplewidth(), track.get_framerate()) 


def crossfade_exp(track1, track2, factor, t):
    p.check_same_params(track1, track2)
    return add(fade_exp(track1, factor), fade_inv(track2, factor), t, a1=1, a2 =1)

