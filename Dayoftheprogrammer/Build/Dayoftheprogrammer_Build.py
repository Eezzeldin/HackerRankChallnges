'''
Author: Emad Mohamed
Date  : Saturday 1st September 2018
Challenge: Day of the Programmer
This use case applies the parrallel worlds analogy in which the code should handle the transitions between the math in one domain to the other.
'''


## Define Julian or Gregorian
def is_JulianGregorian(year):
    print ("Start1: Getting Calender")
    calender = ''
    print ("Determining Calender")
    if   year >= 1918 : calender = 'Gregorian'
    elif year <= 1917 : calender  = 'Julian'
    print ("End1: Got Calender")
    print ("==" *40)
    return calender

## Define a LeapYear
def is_LeapYear (year,calender):
    print ("Start2: Finding out if it is Leap Year")
    def is_Divisible (year,x):
        Divisible = False
        if year % x is 0:Divisible = True
        return  Divisible
    LeapYear = False
    if   calender is 'Julian'    and  is_Divisible (year,4) : LeapYear = True
    elif calender is 'Gregorian' and (is_Divisible (year,400) or  (is_Divisible (year,4) and  not is_Divisible (year,100))) :  LeapYear = True
    print ("End2: It was determined if it was Leap Year or Not")
    print ("==" *40)
    return LeapYear

def get_FebruaryDays (LeapYear):
    print ("Start3: Finding number of days in February")
    FebruaryDays = 29
    if LeapYear: FebruaryDays = 28
    print ("End3 : Found Number of days in February")
    print ("==" *40)
    return FebruaryDays

def get_DayofProgrammer(FebruaryDays):
    print ("Start4: Finding Day of Programmer")
    DayofProgrammer = 13
    if FebruaryDays is 28 :  DayofProgrammer = 12
    print ("End4: Found Day of Programmer")
    print ("==" *40)
    return DayofProgrammer


def get_DateofProgrammer(year):
    if year != 1918:
        print ("Not 1918 use case")
        print ("==" *40 )
        print ("Time to get Date of Programmer")
        calender = is_JulianGregorian(year)
        print ("Calender Has Been Determined as: ", calender)
        LeapYear = is_LeapYear (year,calender)
        print ("Was it LeapYear? : ", LeapYear)
        FebruaryDays = get_FebruaryDays (LeapYear)
        print ("Number of Days in Februay: " , FebruaryDays)
        DayofProgrammer = get_DayofProgrammer(FebruaryDays)
        print ("Is it the 13th or 12t? " , DayofProgrammer)
        YearofProgrammer= year
        MonthofProgrammer= '09'
        DateofProgrammer = str(DayofProgrammer) +'.09.' + str(year)
        print ("Returning Date of Programmer:" , DateofProgrammer )
        print ("=="* 40)
        print ("Results: ",
        "Year Entered :"+ str (year),
        "Not 1918 use case",
        "Calender Has Been Determined as: " + str(calender),
        "Date of Programmer: "              + str(DateofProgrammer),
        "Was it LeapYear? : "               + str(LeapYear),
        "Number of Days in Februay: "       + str(FebruaryDays),
        "Is it the 13th or 12t? "           + str(DayofProgrammer),
        "Returning Date of Programmer:"     + str(DateofProgrammer)
        ,sep= '\n')
        print ("The End")
        print ("==" * 40 )
    else:
        print ("1918 use case")
        DateofProgrammer = '26.09.1918'
    return DateofProgrammer


year0            = 2017
year1            = 2016
year2            = 1918
DayofProgrammer0  = get_DateofProgrammer(year0)
print (DayofProgrammer0,'\n')
DayofProgrammer1  = get_DateofProgrammer(year1)
print (DayofProgrammer1,'\n')
DayofProgrammer2  = get_DateofProgrammer(year2)
print (DayofProgrammer2,'\n')
