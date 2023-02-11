'''
STDIN   Function
-----   --------
3       q = 3
aaab    s = 'aaab' (first query)
baa     s = 'baa'  (second query)
aaa     s = 'aaa'  (third query)

3
aaab
baa
aaa

'''

'''
10
quyjjdcgsvvsgcdjjyq
hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh
fgnfnidynhxebxxxfmxixhsruldhsaobhlcggchboashdlurshxixmfxxxbexhnydinfngf
bsyhvwfuesumsehmytqioswvpcbxyolapfywdxeacyuruybhbwxjmrrmjxwbhbyuruycaexdwyfpaloyxbcpwsoiqtymhesmuseufwvhysb
fvyqxqxynewuebtcuqdwyetyqqisappmunmnldmkttkmdlnmnumppasiqyteywdquctbeuwenyxqxqyvf
mmbiefhflbeckaecprwfgmqlydfroxrblulpasumubqhhbvlqpixvvxipqlvbhqbumusaplulbrxorfdylqmgfwrpceakceblfhfeibmm
tpqknkmbgasitnwqrqasvolmevkasccsakvemlosaqrqwntisagbmknkqpt
lhrxvssvxrhl
prcoitfiptvcxrvoalqmfpnqyhrubxspplrftomfehbbhefmotfrlppsxburhyqnpfmqlaorxcvtpiftiocrp
kjowoemiduaaxasnqghxbxkiccikxbxhgqnsaxaaudimeowojk

1
8
33
23
25
44
20
-1
14
-1
'''


'''
''.join([test_str[i] for i in range(len(test_str)) if i != 2])
'''

'''
V5 : time out problem
multiple index iteration
'''

'''
V6 : applymap
'''

import numpy as np
from time import time



def removechar (s,i):
    #removes char by index from string
    return s [:i] + s [i+1:]

def reversestring (s):
    return s [::-1]

def is_palindromeIndex(s):
    return s == reversestring (s)

def ur_ispalindromeIndex (s,i):
    #upon removal of char is palindromeIndex?
    #return boolean
    if is_palindromeIndex (removechar (s,i)):
        return i
    else :
        pass

    #s_list     = s.split ()
    #index_list = [i for i in range (len (s_list))]


s           = "aaab"
index_list  = [i for i in range (len (s))]
index_array = np.array (index_list)

print (index_array)
print (index_list)

st        = time ()
def temp (i) : return i + 1
map_fun = list (map ( temp, index_list))
e        = time ()
print (map_fun , e-st)

st        = time ()
vec_temp = np.vectorize (temp)
e        = time ()
print (vec_temp (index_array) , e-st)

st        = time ()
map_func_s = list (map ( removechar, [s for i in range (len (s))] ,index_list))
e        = time ()
print (map_func_s,e - st)

st       = time ()
for i in range (len (s)):
    removechar (s , i)
e        = time ()
print (e - st)


st           = time ()
map_func_s   = list ( map ( ur_ispalindromeIndex  , [s for i in range (len (s)) ] , [i for i in range ( len (s) ) ] ) )
e            = time ()
print (map_func_s , e-st)

st           = time ()
for i in range (len (s)):
    ur_ispalindromeIndex (s,i)
e            = time ()
print (e - st)


'''
def palindromeIndex(s):
    # Write your code here

    #Constants
    #c1               = is_palindromeIndex(s) #condition 1
    loop_range       = len (s) // 2          #divide s in two
    last_char_index  = len (s) - 1

    if is_palindromeIndex(s) :
        return -1
    else:
        for i in range (loop_range):
            forward_index = i
            backward_index = last_char_index - i

            if ur_ispalindromeIndex (s,i):
                return forward_index
            elif ur_ispalindromeIndex (s,i):
                return backward_index

    return -1
'''
