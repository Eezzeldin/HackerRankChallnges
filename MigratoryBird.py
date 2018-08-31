'''
Author : Emad Ezzeldin
Date   : Tuesday August 21st 2018
Challenge : MigratoryBird
'''

input_Sample = [1, 4, 4, 4, 5, 3,3,5,5,5]
repeated     = {1: 0 , 2:0 , 3:0 , 4:0 , 5:0}

for element in input_Sample:
    repeated [element] += 1
print (repeated)

## Max Count Operations: All Operations here are on a list of 5 elemnts only so it's very cheap.
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
