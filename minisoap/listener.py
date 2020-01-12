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

from threading import Thread, Event

## Listener class
#
# A killable thread
class Listener(Thread):
    def __init__(self):
        Thread.__init__(self)
        self._kill = Event()
        self._listening = False

    def __str__(self):
        return 'Listener: '+self.__class__.__name__ + (' listening...' if self._listening else '')
    ## Kill the Thread
    #
    def kill(self):
        self._kill.set()
    def killed(self):
        return self._kill.isSet()