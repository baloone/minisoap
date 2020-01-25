from minisoap.stream import Fallback, Rotation
from minisoap.generators import Constant
import numpy as np


def test_fallback():
    fb = Fallback(*[Constant(i, .5) for i in range(5)])
    i = 0
    b = True
    for block in fb:
        if block is None:  # Track change
            i += 1
            continue
        if np.count_nonzero(block != i) > 0:
            b = False
            break
    assert b


def test_rotation():
    Rot = Rotation(*[Fallback(*[Constant(2**i*3**j, .5)
                                for i in range(5)]) for j in range(5)])
    i, j = 0, 0
    b = True
    for block in Rot:
        if block is None:  # Track change
            if j == 4:
                i += 1
                j = 0
            else:
                j += 1
            continue
        if np.count_nonzero(block != 2**i*3**j) > 0:
            b = False
            break
    assert b
