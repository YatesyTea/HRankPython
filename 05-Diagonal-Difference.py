#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr[0])
    total1, total2 = 0, 0
    for x in range (0, n):
        for y in range(0,n):
            if (x==y):
                total1+=arr[x][y]
                print("1 " + str(arr[x][y]))
            if (x+y == n-1):
                total2+=arr[x][y]
                print("2 " + str(arr[x][y]))

    result = abs(total1 - total2)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
