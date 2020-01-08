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

from .stream import Stream
import soundcard as sc

class Microphone(Stream):
    def __init__(self, mic, chunk = None, samplerate = None, channels=None):
        Stream.__init__(self, chunk, samplerate, channels)
        if not mic.record : raise Exception("Not a microphone")
        self._mic = mic

    def __str__(self):
        return 'Microphone('+self._mic.__str__()+')'
    def __iter__(self):
        with self._mic.recorder(self.samplerate, self.channels) as rec:
            self._rec = rec
        return self
    def __next__(self):
        if self._rec._samplerate != self.samplerate:
            with self._mic.recorder(self.samplerate, self.channels) as rec:
                self._rec = rec
        data = self._rec.record(self.chunk)
        print(data)
        return data
        

