'''
author : Emad Ezzeldin
Date   : Sunday August 19th 2018
Challenge: Breaking the Records

- It should teach how to do computation within the
elements of a list.
- Also how can this computation affect on an outside
variable. Like an Event Listener
'''

##Initialize
Game_Index = 0
Maria_Score= 0
Max_Record = 0
Min_Record = 0
Max_Count  = 0 #Counter for Breaking Min
Min_Count  = 0 #Counter for Breaking Max

##Sample Input
Sample_Input= [10,5,20,20,4,5,2,25,1] #9 Games
#1st Game
Game_Index = 0
Maria_Score= 10
Max_Record = 10
Min_Record = 10
Max_Count  = 0
Min_Count  = 0
#2nd Game
Game_Index = 1
Maria_Score=5
Max_Record =10
Min_Record =10
if Maria_Score < Min_Record:
    Min_Record = Maria_Score #Update Record
    Min_Count +=1            #Increment
elif Maria_Score > Max_Record:
    Max_Record = Maria_Score
    Max_Count +=1
print ('Min_Count:',Min_Count,'Max_Count:',Max_Count,'Min_Record:',Min_Record,'Max_Record:',Max_Record)
