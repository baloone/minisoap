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
from .stream import Stream
from .clock import Clock
from .player import Player

class Builtins:
    '''
    Write all builtins functions here
    '''
    def __init__(self):
        self.clock = Clock()
    def tst(self, *args):
        print('hey', *args)
    def open(self, filepath):
        return Song(filepath)
    def play(self, stream_or_player):
        if not isinstance(stream_or_player, (Stream, Player)): raise TypeError('Expected stream or player')
        if isinstance(stream_or_player, Stream):
            stream = stream_or_player
            pl = Player(stream)
            pl.start()
        else: 
            pl = stream_or_player
            pl.play()
        return pl
    def pause(self, player):
        player.pause()
    def stop(self, player):
        player.stop()
