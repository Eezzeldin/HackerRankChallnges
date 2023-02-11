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
    return ur_ispalindromeIndex (removechar (s,i),i)

    #s_list     = s.split ()
    #index_list = [i for i in range (len (s_list))]






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
