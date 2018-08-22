'''
Author : Emad Ezzeldin
Date   : Tuesday August 21st 2018
Challenge : MigratoryBird
'''

input_Sample = [1, 4, 4, 4, 5, 3,3,5,5,5]
l            = len (input_Sample)
pairs        = []
repeated     = {1: 0 , 2:0 , 3:0 , 4:0 , 5:0}
#for element in input_Sample: repeated [element] = 0
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
    b            = ii == ij # condition
    return b

for element in input_Sample:
    repeated [element] += 1
print (repeated)        
'''
## Slide Variable Sized Window
for i in range (i1,i2):
    ii=  input_Sample [i]                              #current value of i
    for j in range (i+1,j2):                           #Slide j
        ij           =  input_Sample [j]               #current value of j
        print (ii)
        if DivisbleSum (ii,ij):
            pairs.append ([ii,ij]) # Run Logic
            repeated[ii] = repeated[ii] + 1
    print (repeated)                                      #Print output

#print (max(repeated))
'''


## Max Count Operations
#Get List of Counts
Counts = [element for element in repeated.values()]
print (Counts)
#Find Max Count
MaxC  = max (Counts)
print (MaxC)
## Logic
#Find Elements with Max Count : Find Keys where values are MaxC
MaxCE = [element for element in repeated if repeated [element] is MaxC]
print (MaxCE)
#Check if they are more than one
Final = []
if len (MaxCE) >1 :
    Final =  min (MaxCE)
#If More than one return their min.
else:
    Final = MaxCE[0]
print (Final)

'''
count = [0]*5
for t in   map (int,input_Sample):
    count[t] += 1
print (count)
print(count.index(max(count)))
'''
