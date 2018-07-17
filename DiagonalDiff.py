#!/bin/python3

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    #
    # Write your code here.
    #
    print (a)
    rowsnum = len (a)
    colnum  = rowsnum
    LeftD   = 0
    RightD  = 0
    for i in range (rowsnum):
        print (a[i] [i])
        print (a[i] [rowsnum-i-1])
        LeftD  += a [i] [i]
        RightD += a[i] [rowsnum-i-1]
    DD     = LeftD - RightD
    return abs (DD)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
