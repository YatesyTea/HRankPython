#!/bin/python3

import math
import os
import random
import re
import sys

# Prints out Array fractions given length of arr.
def printArrayFractions(countArr, length):
    for x in range (0, len(countArr)):
        if countArr[x] == 0:
            print(countArr[x])
        else:
            print(round(countArr[x]/length,6))    

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    countArr = [0,0,0]
    for x in range (0,len(arr)):
        if (arr[x] == 0):
            countArr[2] += 1
        elif (arr[x] < 0):
            countArr[1]+= 1
        else:
            countArr[0]+= 1
    
    printArrayFractions(countArr,len(arr))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
