# Copyright (C) 2019 Mohamed H
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

from .song import Song
from .writer import Writer
from .stream import Stream
from .clock import Clock
from .player import Player
from .microphone import Microphone
from .generators import Silence, Sine
from .playlist import Playlist

## Builtins class
#
# Contains and execute all the language operations
class Builtins:
    '''
    Write all builtins functions here
    '''
    def __init__(self):
        self.clock = Clock()
    
    ## @var clock
    # A clock for handeling timeouts between calls in ms 
    
    def log(self, *args):
        """!
        Print variables
        
        @param **args Any variable to print
        """
        print(*args)
    
    def open(self, filepath):
        """!
        Open a song
        
        @param filepath The path to the song
        """
        return Song(filepath)
    
    def write(self, stream, output_path):
        """!
        Writes a stream to a file
        
        @param stream The stream
        @param output_path The path to the output
        """
        w = Writer(stream, output_path)
        w.run()
        return w
    
    
    def play(self, stream_or_player):
        """!
        Play a stream or a player
        
        @param stream_or_player The stream or the player
        """
        if not isinstance(stream_or_player, (Stream, Player)):
            raise TypeError('Expected stream or player')
        if isinstance(stream_or_player, Stream):
            stream = stream_or_player
            pl = Player(stream)
            pl.start()
        else: 
            pl = stream_or_player
            pl.play()
        return pl
    
    
    def pause(self, player):
        """!
        Pause a player
        
        @param player The player
        """
        player.pause()
    
    def all_mics(self):
        """!
        Transform all microphones to streams
        
        """
        from soundcard import all_microphones
        return [Microphone(mic) for mic in all_microphones()]
    
    def get(self, i, array):
        """!
        Get element from array
        
        @param i Index of element
        @param array The array
        """
        try:
            return array[int(i)]
        except:
            return None
    
    
    def silence(self, duration=float('inf'), chunk = None, samplerate = None, channels=None):
        """!
        Generate a silent wave
        
        @param duration The duration of the wave in seconds (optional)
        @param chunk The number of chunks (optional)
        @param samplerate The sample rate of the wave (optional)
        @param channels The number of channels (optional)
        """
        return Silence(duration=float('inf'), chunk = None, samplerate = None, channels=None)

    
    def sine(self, freq=440, amplitude=1, duration=None, chunk = None, samplerate = None, channels=None):
        """!
        Generate a sine wave
        
        @param freq The frequency of the wave (optional)
        @param amplitude The wave amplitude (optional)
        @param duration The duration of the wave in seconds (optional)
        @param chunk The number of chunks (optional)
        @param samplerate The sample rate of the wave (optional)
        @param channels The number of channels (optional)
        """
        return Sine(freq=440, amplitude=1, duration=None, chunk = None, samplerate = None, channels=None)

    def playlist(self, dir_path, chunk = None, samplerate = None, channels=None):
        """!
        Open a playlist
        
        @param dir_path The directory path to the playlist
        @param chunk The size of the chunk (optional)
        @param samplerate The sample rate of the wave (optional)
        @param channels The number of channels (optional)
        """
        return Playlist(dir_path, chunk = None, samplerate = None, channels=None)
