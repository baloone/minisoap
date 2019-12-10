from .stream import Stream
from pathlib import Path

class Song(Stream):
    def __init__(self, filename):
        exts = ["wav", "mp3", "flac", "aac", "m4a", "ogg"]
        if not filename.split('.')[-1] in exts : raise Exception("Extension not recognized")
        self.path = Path(filename).absolute()


