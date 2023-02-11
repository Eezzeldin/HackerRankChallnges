
def sort_index (grid_index_list) :
    lists =  list (map (sorted , grid_index_list))
    lists = list (map ("".join ,  lists))
    return   lists

def is_True (X,Y):return X == Y
def is_True_lists (list1,list2): return all (map (is_True ,list1 , list2 ))

'''
#read and flip a matrix
#col1 : 0s index of all rows
'''
def get_i (somestringlist,i):
    #print (i,somestringlist)
    return somestringlist [i]
def get_col_i (grid,j):
    #print (grid , j )
    return "".join (list (map (get_i , grid , [j for p in range ( len (grid))] )))
def t_grid (grid):
    grid_list  =   [grid for i in range (len (grid))]
    index_list =   [i    for i in range (len (grid[0]))]
    #print (grid, len (grid))
    #print (grid_list)
    #print (index_list)
    return list (map (get_col_i , grid_list , index_list))


    
