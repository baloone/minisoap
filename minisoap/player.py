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

from threading import Thread
from .stream import Stream
import soundcard as sc
import time

class Player(Thread):
    def __init__(self, stream):
        if not isinstance(stream, Stream): raise TypeError
        Thread.__init__(self)
        self.stream = stream
        self._play = True
        self.sp = sc.default_speaker()
        self._stop = False
        self._ended = False
    def run(self):
        with self.sp.player(samplerate=self.stream.samplerate,
            channels=self.stream.channels) as sp:
            for block in self.stream:
                while not self._play:
                    if self._stop: break
                    time.sleep(0.1)
                if self._stop: break
                sp.play(block)
        self._ended = True

    def pause(self):
        self._play = False

    def play(self):
        self._play = True

    def stop(self):
        self._stop = True
