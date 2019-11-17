

# # Preconditions module
# 
# This module should contain all of the checking function that raise certain exceptions or errors. It will help modularise the code and make it cleaner all sort of checks can be added here.

# Include necessary imports here



import math as m
import sys


# The method check verifies if the value satisfies a certain predicate if not it raises a ValueError with details as specification of why value was wrong. 




def check(value, predicate=lambda x: x, details='bad value for this function'):
    if (not(predicate(value))): 
        raise ValueError(details)



# This method is a special case of check as it checks if a value is in a certain range or not.



def check_in_range(value, startInclusive=0, endExclusive= m.inf): 
    check(value, lambda x: x >= startInclusive and x < endExclusive)
    
    

def check_same_params(track1, track2):
    get_params = lambda x: (x.get_nchannels(), x.get_samplewidth(), x.get_framerate())
    check((track1, track2), predicate=lambda x: get_params(x[0]) == get_params(x[1]), details="non compatible Tracks")

# error printing method 
    
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

