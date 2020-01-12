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
from .stream import Stream, Mix, Fallback, Rotation
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
        pass

    
    def all_functions(self):
        """!
        Prints all available functions
        """
        return "\n\n".join([i+": "+getattr(Builtins, i).__doc__[2:].strip() for i in dir(self) if i[0]!="_"])
    
    def open(self, filepath):
        """!
        Opens a song
        
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
        w.start()
        return w
    
    
    def play(self, stream_or_player):
        """!
        Plays a stream or a player
        
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
        Pauses a player
        
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
    
    
    def silence(self, duration=float('inf')):
        """!
        Generates a silent wave
        
        @param duration The duration of the wave in seconds (optional)
        """
        return Silence(duration=float('inf'))

    
    def sine(self, freq=440, amplitude=1, duration=None):
        """!
        Generates a sine wave
        
        @param freq The frequency of the wave (optional)
        @param amplitude The wave amplitude (optional)
        @param duration The duration of the wave in seconds (optional)
        """
        return Sine(freq=440, amplitude=1, duration=None)

    def playlist(self, dir_path, loop=0.0, transition = None):
        """!
        Opens a playlist
        
        @param dir_path The directory path to the playlist
        @param loop 0 if the playlist doesn't loop 
        @param dir_path The directory path to the playlist
        """
        print(loop > 0)
        return Playlist(dir_path, loop > 0, transition)
    
    def shuffle(self, playlist):
        """!
        Shuffles a playlist
        
        @param playlist The playlist to shuffle
        """
        playlist.shuffle()
        return playlist
    def fallback(self, *streams):
        """!
        Returns a Fallback
        
        @params ...streams The streams
        """
        return Fallback(*streams)
    
    def rotation(self, *streams):
        """!
        Returns a Rotation
        
        @params ...streams The streams
        """
        return Rotation(*streams)

    def mix(self, stream, bgstream=None, scalar=.5):
        """!
        Mixes between two streams
        
        @param stream The main stream
        @param bgstream The background stream (optional)
        @param scalar The multiplier (default value : .5)
        """
        return Mix(stream, bgstream, scalar)
