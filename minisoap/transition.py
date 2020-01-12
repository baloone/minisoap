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
import numpy as np

## Returns a convexe combination of two numpy vectors
#
# @param p1 First vector
# @param p2 Second vector
# @param t Scalar value
def bar(p1, p2, t):
    return t*p1+(1-t)*p2


## Transition class
#
# Realize transition between two streams
class Transition:
    def __init__(self, table=[]):
        self.duration = 0 if table == [] else max([i[0] for i in table])
        self._table = sorted(table)
    
    ## @var duration
    # Duration of the transition
    
    ## @var _table
    # Next values (transition table)
    
    ## Makes the transition between of samples in _table
    #
    # @param t Time of transition
    def amplitude(self, t):
        """
        Linear approximation of the transition table
        Returns amplitude of the stream which is ending
        t in s
        """
        try:
            i = len(self._table)-1
            while self._table[i][0] > t: i-=1
            t1,a1=self._table[i]
            t2,a2=self._table[i+1]
            return (a2-a1)/(t2-t1)*(t-t1)           
        except:
            return 0
    
    ## String representation of transition objects
    #
    def __str__(self):
        return 'Transition(\n.     '+"\n.     ".join([str(t[0])+"s ->> "+str(t[1]) for t in self._table])+'\n)'
