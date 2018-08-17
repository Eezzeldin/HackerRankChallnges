'''
Author : Emad Ezzeldin
Date   : Tuesday August 7th 2018 , Monday August 13th 2018
Problem: Between 2 Sets
Progress:
=========
Now stuck with one piece which is how to apply a function to evey element in a list.
I found this source on it though:
https://stackoverflow.com/questions/1790520/how-to-apply-a-logical-operator-to-all-elements-in-a-python-list/1790532
'''


m = 0 #1<= m <=10
n = 0 #1<= n <=10

a = []#1<= a <=100
b = []#1<= b <=100


m,n = 2,3

a,b = [2,4],[16,32,96]


#for i in range (m): print (a[i])
#for j in range (n): print (b[j])

#for i in range (1,101): print (i)
#for j in range (1,101): print (j)


a1        = a ==4
condition = all (a)
#print (condition)

inbetween = [i for i in range (1,101) for A in a for B in b if i % A is 0 and B%i is 0]
#print (inbetween)
#print (set (inbetween))

'''
This Section is dedicated for knowing if integer x between 1 and 100 is a factor of every element in the list
I/P: x,mylist
O/P: x is a factor of every element in the list
'''
##Base Function
def isFactor (x,y): return x%y == 0
#print (isFactor (6,2))

##Apply Function map (alist,lambda)
def isFactor_list (x,mylist): return [isFactor (x,y) for y in mylist]

##List Aggregation Function : all(list)
def isFactor_alllist(x,mylist): return all (isFactor_list (x,mylist))


'''
Reversing Sides
'''
##Apply Function Map in reverse
def list_isFactor (x,mylist): return [isFactor (y,x) for y in mylist]

##List Aggregation Function : all(list)
def alllist_isFactor(x,mylist): return all (list_isFactor (x,mylist))


'''
Between the 2 sets
6,[2,6],[24,36]
'''
##Mulit-List Aggregation  : all (list1) and all(list2)
def between2sets(x,mylist1,mylist2): return isFactor_alllist(x,mylist1) and alllist_isFactor (x,mylist2)
print (between2sets(6,[2,6],[24,36]))


'''
All integers between min of one set and max of the other one
'''
## Find Minimum of a set
def getMin (mylist): return min (mylist)
#print (getMin([24,36]))

## Find Maximum of a set
def getMax (mylist) : return max (mylist)
#print (getMax([24,36]))

## Loop through a range of integers
def LoopThrough (mylist1,mylist2):
    mymin = getMin (mylist1)
    mymax = getMax (mylist2)
    return [i for i in range (mymin,mymax+1)]
#print (LoopThrough([2,6],[24,36]))


'''
Now this is the Finale , this is the main function
'''
mylist1    = [2,6]
mylist2    = [24,36]
myintegers =  LoopThrough(mylist1 ,mylist2)
between2sets= [x for x in myintegers if between2sets(x,mylist1,mylist2)]
print (between2sets)
