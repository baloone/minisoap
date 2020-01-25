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
import sys

if 'pytest' in sys.argv[0]:
    class Microphone(Stream):
        pass
else:
    import soundcard as sc

    # Microphone Stream
    #
    # This object represents the Microphone as a Stream
    class Microphone(Stream):

        def __init__(self, mic=None):
            if mic is None:
                try:
                    mic = sc.default_microphone()
                except Exception:
                    raise Exception("No microphones avalaible")
            Stream.__init__(self)
            if not mic.record:
                raise Exception("Not a microphone")
            self._mic = mic

        # @var _mic
        # Default microphone from soundcard library

        # Start recording
        #
        def _gen(self):
            with self._mic.recorder(self.samplerate, self.channels) as rec:
                while True:
                    yield rec.record(self.chunk)

        # Iterate over the stream
        #
        def __iter__(self):
            self.__gen = self._gen()
            return self

        # String representation of microphone
        #
        def __str__(self):
            return 'Microphone('+self._mic.__str__()+')'

        # Next function of the iterator
        #
        def __next__(self):
            return next(self.__gen)
