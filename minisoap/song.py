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

from .stream import Stream
from pathlib import Path
from audioread.ffdec import FFmpegAudioFile
import os

class Song(Stream):
    def __init__(self, filename, chunk = 4096):
        self.chunk = chunk
        exts = ["wav", "mp3", "flac", "aac", "m4a", "ogg"]
        if not filename.split('.')[-1] in exts : raise Exception("Extension not supported")
        self.path = Path(filename).absolute()
        if not os.path.exists(self.path): raise Exception("File not found")
        self.f = FFmpegAudioFile(self.path, chunk)
    def __str__(self):
        return 'Song('+self.path.__str__()+')'

