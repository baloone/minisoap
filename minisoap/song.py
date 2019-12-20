from .stream import Stream
from pathlib import Path
import audioread, os

class Song(Stream):
    def __init__(self, filename):
        exts = ["wav", "mp3", "flac", "aac", "m4a", "ogg"]
        if not filename.split('.')[-1] in exts : raise Exception("Extension not recognized")
        self.path = Path(filename).absolute()
        if not os.path.exists(self.path): raise Exception("File not found")
        with audioread.audio_open(filename) as f:
            self.f = f
    def __str__(self):
        return 'Song('+self.path+')'

