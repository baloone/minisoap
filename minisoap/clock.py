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

from datetime import datetime, timedelta

## Clock class
#
# Clock used for timeouts in executions
class Clock:
    
    def __init__(self):
        self.exs = []
    
    ## @var exs
    # List of clock's stored executions
    
    ## Run and execute instructions
    #
    def step(self):
        t = datetime.now()
        l = []
        while len(self.exs):
            d, f = self.exs.pop()
            if d <= t: f()
            else: l.append((d, f))
        self.exs = l
        
    ## Add execution to clock
    #
    # @param f The function to execute
    # @param d Timeout in milliseconds 
    def wait(self, f, d=0): # d duration in ms
        self.exs.append((datetime.now()+timedelta(milliseconds=d), f))

