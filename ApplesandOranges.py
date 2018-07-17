#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    class Tree:
        def __init__(self,position):
            self.position = position

        def getTreePosition(self):
            return self.position

        def printTreePosition(self):
            print ('Tree Position:', self.getTreePosition())

    #T1 = Tree(5)
    #T1.printTreePosition()


    class House:
        def __init__(self,TreePosition,start,end):
            Tree.__init__(self,TreePosition)
            self.start = start
            self.end   = end

        def getStart(self):
            return self.start

        def getEnd(self):
            return self.end

        def printHouse(self):
            print ('House is between:','start:',self.getStart(),'end:',self.getEnd())

    #h1 = House (5,7,11)
    #h1.printHouse()

    class Apple:
        def __init__(self,HStart,HEnd,TreePosition,Distance):
            Tree.__init__(self,TreePosition)
            House.__init__(self,TreePosition,HStart,HEnd)
            self.Distance = Distance

        def getCurrentLocation(self):
            return Tree.getTreePosition(self) + self.Distance

        def isAppleonHouse(self):
            self.currentLocation = self.getCurrentLocation()
            if House.getStart(self) <=self.currentLocation <= House.getEnd(self): return True
            else : return False

        def printCurrentLocation(self):
            print ('Apple Current Location:' , self.getCurrentLocation())

        def printIsFruitonHouse(self):
            #print ('TreeLocation',Tree.printTreePosition(self))
            #print ('HouseLocation',House.printHouse(self))
            print ('If Fruit on House:',self.isAppleonHouse())

    #a1 = Apple (7,11,5,-2) #a:5  , D: -2 , Start:7 , End:11
    #a1.getCurrentLocation()
    #a1.printCurrentLocation()
    #a1.printIsFruitonHouse()
    #a2 = Apple (7,11,5,2) #a:5  , D: 2 , Start:7 , End:11
    #a2.getCurrentLocation()
    #a2.printCurrentLocation()
    #a2.printIsFruitonHouse()


    #for apple in apples : Apple(s,t,a,apple).printIsFruitonHouse()
    #for orange in oranges: Apple(s,t,b,orange).printIsFruitonHouse()

    print (len([Apple(s,t,a,apple).isAppleonHouse() for apple in apples if Apple(s,t,a,apple).isAppleonHouse() is True]))
    print (len ([Apple(s,t,b,orange).isAppleonHouse() for orange in oranges if Apple(s,t,b,orange).isAppleonHouse() is True]))


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
