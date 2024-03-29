'''
author:Emad
Date  :Friday June 22nd 2018
Challenge: HackerRank Kangroo
Input    : 0 2 5 3    , x1 , v1 , x2, v2
O/P      : No
'''
import math
import os
import random
import re
import sys

def didtheystarttogether(x1,x2):
    theydid = False
    if x1 == x2 :
        theydid = True
    return theydid

def whoisfaster (v1,v2):
    Faster = ''
    if v1 > v2:
        Faster = 'K1'
    elif v1 < v2:
        Faster = 'K2'
    return Faster

def whoisinfront(x1,x2):
    Infront = ''
    if x1 > x2:
        Infront = 'K1'
    elif x1 < x2 :
        Infront = 'K2'
    return Infront

def ratio(x1,v1,x2,v2):
    return (x1-x2) % (v1-v2)

#21 6 47 3
# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if didtheystarttogether(x1,x2) is True :
        return ('YES')
    elif whoisfaster (v1,v2) is whoisinfront(x1,x2) or v1 == v2:
        return ('NO')
    elif ratio(x1,v1,x2,v2) is 0:
        return ('YES')
    else:
        return ('NO')
  
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    #fptr.write(result + '\n')

    #fptr.close()
