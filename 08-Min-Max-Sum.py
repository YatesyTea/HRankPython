#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minVal, maxVal, total = 100000000000000000000,0,0
    for x in range(0, len(arr)):
        total += arr[x]
        if arr[x] < minVal:
            minVal = arr[x]
        if arr[x] > maxVal:
            maxVal = arr[x]
    
    print (f"{total-maxVal} {total-minVal}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
