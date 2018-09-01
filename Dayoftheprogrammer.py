'''
Author: Emad Mohamed
Date  : Saturday 1st September 2018
Challenge: Day of the Programmer
This use case applies the parrallel worlds analogy in which the code should handle the transitions between the math in one domain to the other.
'''


##Define a LeapYear
def is_LeapYear (year,calender):
    def is_Divisible (year,x): return if year % x is 0 # Year Divisible by x
    LeapYear = False
    if   calender is 'Julian'    and  is_Divisible (year,x) : LeapYear = True
    elif calender is 'Gregorian' and (is_Divisible (year,400) or  (is_Divisible (year,4) and  not is_Divisible (year,100))) :  LeapYear = True
    return LeapYear

##Define Julian or Gregorian
def is_JulianGregorian(year):
    calender = ''
    if   year >= 1918 : calender = 'Gregorian'
    elif year <= 1917: calender  = 'Julian'
    return calender

                
