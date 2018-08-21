'''
author: Emad Ezzeldin
Date  : Monday August 20th 2018
Challenge: Divisible Sum Pairs
'''

## Variables
input_Sample = [1, 3, 2, 6, 1, 2]
l            = len (input_Sample)
pairs        = []
i            = 0
j            = 0
i1           = 0     # fixed starting index
i2           = l - 1 # end stop index
j1           =  1    # sliding starting index
j2           =  l    # sliding ending index
k            = 3

## Operations
def DivisbleSum (ii,ij):
    m            =  ii  + ij  #math
    b            = m % k == 0 # condition
    return b

## Slide Variable Sized Window
for i in range (i1,i2):
    ii=  input_Sample [i]                              #current value of i
    for j in range (i+1,j2):                           #Slide j
        ij           =  input_Sample [j]               #current value of j
        print (ii , ij)
        if DivisbleSum (ii,ij): pairs.append ([ii,ij]) # Run Logic
    print (pairs)                                      #Print output
