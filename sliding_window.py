'''
author    : Emad Ezzeldin
Date      : Monday August 20th 2018
Challenge : Birthday Chocolate
'''

##Variables
Input_Sample = [1,2,1,3,2]     # 5 bars of chocolate with 1 written on them
m            = 2               # Window Size
d            = 3               # Desired Total
s            = 1               # Slide_Size
m0           = 0               # Window Start index
w            = []              # Window
counter      = 0
iterations   = len (Input_Sample) - (m -1) #Number of iterations
print ("iterations:" , iterations)

##Initiatlization: Build Window , Math , Logic (event detection) and Counter (event listener)
w = [Input_Sample [i] for i in range (m0,m0+m)]
print ("Window:",w)
if sum (w) == d : counter+=1
print ("counter:",counter)

##Looping
#for loop
for i in range (iterations-1):
    #Slide
    m0+=s
    w = [Input_Sample [i] for i in range (m0,m0+m)]
    print ("Window:",w)
    if sum (w) == d : counter+=1
    print ("counter:",counter)
