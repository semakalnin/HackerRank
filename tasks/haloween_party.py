import math
import os
import random
import re
import sys

#
# Complete the 'halloweenParty' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER k as parameter.
#

def halloweenParty(k):
    horizontal_cuts = k // 2
    vertical_cuts = k - horizontal_cuts
    pieces = horizontal_cuts * vertical_cuts
    return pieces
