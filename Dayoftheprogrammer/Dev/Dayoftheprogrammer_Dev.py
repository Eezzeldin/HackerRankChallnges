'''
Author: Emad Mohamed
Date  : Saturday 1st September 2018
Challenge: Day of the Programmer
This use case applies the parrallel worlds analogy in which the code should handle the transitions between the math in one domain to the other.
'''


## Define Julian or Gregorian
def is_JulianGregorian(year):
    calender = ''
    if   year >= 1918 : calender = 'Gregorian'
    elif year <= 1917 : calender  = 'Julian'
    return calender

## Define a LeapYear
def is_LeapYear (year,calender):
    def is_Divisible (year,x):
        Divisible = False
        if year % x is 0:Divisible = True
        return  Divisible
    LeapYear = False
    if   calender is 'Julian'    and  is_Divisible (year,4) : LeapYear = True
    elif calender is 'Gregorian' and (is_Divisible (year,400) or  (is_Divisible (year,4) and  not is_Divisible (year,100))) :  LeapYear = True
    return LeapYear

def get_FebruaryDays (LeapYear):
    FebruaryDays = 29
    if LeapYear: FebruaryDays = 28
    return FebruaryDays

def get_DayofProgrammer(FebruaryDays):
    DayofProgrammer = 13
    if FebruaryDays is 28 :  DayofProgrammer = 12
    return DayofProgrammer

def get_DateofProgrammer(year):
    if year is not 1918:
        calender = is_JulianGregorian(year)
        LeapYear = is_LeapYear (year,calender)
        FebruaryDays = get_FebruaryDays (LeapYear)
        DayofProgrammer = get_DayofProgrammer(FebruaryDays)
        YearofProgrammer= year
        MonthofProgrammer= '09'
        return str(DayofProgrammer) +'.09.' + str(year)
    else:
        return '26.09.1918'

DayofProgrammer = get_DateofProgrammer(year)
