'''
author: Emad Ezzeldin
Date  : Monday August 20th 2018
Challenge: Divisible Sum Pairs
'''

## Variables
input_Sample = [1, 3, 2, 6, 1, 2]
# long_hit     = [[i,j] for j in input_Sample[1:] for i in input_Sample[:input_Sample.index(j)] if (i+j) % 3 is 0]
# print (long_hit)
# combinations     = [[i,input_Sample[j]] for j in range(0,5,-1) for i in range (0,j-1)]
# print (combinations)
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
#  Logic
def DivisbleSum (ii,ij):
    m            =  ii  + ij  #math
    b            = m % k == 0 # condition
    return b

#  Window Length Forward Expansion
i = i1                   # Fixing i at start point
ii=  input_Sample [i]    #current value of i
for j in range (i+1,j2): #Slide j
    ij           =  input_Sample [j] #current value of j
    print (ii , ij)
    if DivisbleSum (ii,ij): pairs.append ([ii,ij]) # Run Logic
print (pairs)            #Print output
