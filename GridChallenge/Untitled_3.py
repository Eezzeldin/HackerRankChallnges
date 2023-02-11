



def gridsearch (grid):
    n            = len (grid)
    m            = len (grid [0])
    grid [0]     = sorted (grid [0])
    for  in range (1,n):
        grid [i] = sorted (grid [i]) #loop through rows "abc" : ["a","b","c"]
        for j in range (m):          #loop through columns
            if grid [i] [j] 
