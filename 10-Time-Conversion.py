#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Check index which holds A or P of AM/PM in string
    # Then slice string and convert if P, otherwise just remove AM from end.
    if (s[8] == 'P'):
        hour = int(s[0:2])+12
        convert = str(hour) + s[2:8]
    else:
        convert = s[0:7]    
    
    return convert

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
