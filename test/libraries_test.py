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

import subprocess


def test_ffmpeg():
    subprocess.Popen(['ffmpeg', '-version'],
                     stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    assert True
