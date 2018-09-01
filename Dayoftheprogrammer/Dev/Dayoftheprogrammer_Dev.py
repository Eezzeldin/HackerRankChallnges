'''
Author: Emad Mohamed
Date  : Saturday 1st September 2018
Challenge: Day of the Programmer
This use case applies the parrallel worlds analogy in which the code should handle the transitions between the math in one domain to the other.
'''

## Variables
x            = 28
##Constants
DaysinYear   = [i for i in range (1,365+1)]
MonthsinYear = ['January', 'February' , 'March', 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'Novermber' , 'December']
DaysinMonths = {'January':31 , 'February': x , 'March': 31 , 'April':30 , 'May':31 , 'June':30 , 'July':31 , 'August':31 , 'September':30, 'October':31 , 'November':30 , 'December':31}


## Define a LeapYear
def is_LeapYear (year,calender):
    def is_Divisible (year,x): return if year % x is 0 # Year Divisible by x
    LeapYear = False
    if   calender is 'Julian'    and  is_Divisible (year,x) : LeapYear = True
    elif calender is 'Gregorian' and (is_Divisible (year,400) or  (is_Divisible (year,4) and  not is_Divisible (year,100))) :  LeapYear = True
    return LeapYear


## Define Julian or Gregorian
def is_JulianGregorian(year):
    calender = ''
    if   year >= 1918 : calender = 'Gregorian'
    elif year <= 1917 : calender  = 'Julian'
    return calender

def get_FebruaryDays (Leapyear,Calender):
    

## Calender Math
#  return dictionary month to year days.
def get_yeardaysinMonth (Month):
    MonthIndex        =  MonthsinYear.index (Month)
    PreviousMonths    =  MonthsinYear [0:MonthIndex]
    PreviousandthisMonth = PreviousMonths.append(Month)
    MonthYearDaysMax  =  sum ([ DaysinMonths [Month] for Month in PreviousandthisMonth])
    MonthYearDaysMin  =  sum ([ DaysinMonths [Month] for Month in PreviousMonths])
    MonthYearDays     = [i for i in range (MonthYearDaysMin ,MonthYearDaysMax)]
    return MonthYearDays



#Day to Month : if I give you a day in the year index, give me which month is it.


#Day to Month Day: If I give you a day in a year index and the month it is in, which day of the month is it.
