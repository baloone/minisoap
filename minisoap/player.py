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
        sp = self.sp.player(samplerate=self.stream.samplerate)
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
