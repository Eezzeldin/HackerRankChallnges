def get_index (letter):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return alphabets.index (letter)
def alpha_index (grid_list): return list ( map (get_index,grid_list) )
def grid_index (grid_lists): return list (map (alpha_index,grid_lists))

def sort_index (grid_index_list) : return  list (map (sorted , grid_index_list))
def sort_index (grid_index_list) :
    lists =  list (map (sorted , grid_index_list))
    lists = list (map ("".join ,  lists))
    return   lists

def is_True (X,Y):return X == Y
def is_True_lists (list1,list2): return all (map (is_True ,list1 , list2 ))
