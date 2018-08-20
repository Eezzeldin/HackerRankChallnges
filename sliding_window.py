'''
author : Emad Ezzeldin
Date   : Monday August 20th 2018
Challenge : Birthday Chocolate
'''

##Variables
Input_Sample = [1,2,1,3,2]     # 5 bars of chocolate with 1 written on them
m            = 3               # Window Size
d            = 3               # Desired Total
s            = 1               # Slide_Size
m0           = 0               # Window Start index
w            = []              # Window
counter      = 0
iterations   = len (Input_Sample) - (m -1) #Number of iterations
print ("iterations:" , iterations)

##Initiatlization
#Trial 1 :
w = [Input_Sample [i] for i in range (m0,m0+m)]
print ("Window:",w)
if sum (w) == d : counter+=1
print ("counter:",counter)

##Iterations 
#Trial 2 :
m0+=s
w = [Input_Sample [i] for i in range (m0,m0+m)]
print ("Window:",w)
if sum (w) == d : counter+=1
print ("counter:",counter)
#Trial 3 :
m0+=s
w = [Input_Sample [i] for i in range (m0,m0+m)]
print ("Window:",w)
if sum (w) == d : counter+=1
print ("counter:",counter)
