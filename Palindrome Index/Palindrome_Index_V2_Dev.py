'''
STDIN   Function
-----   --------
3       q = 3
aaab    s = 'aaab' (first query)
baa     s = 'baa'  (second query)
aaa     s = 'aaa'  (third query)
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

#lst = [10, 11, 12, 13, 14, 15]
#lst.reverse()
#print("Using reverse() ", lst)
#print("Using reversed() ", list(reversed(lst)))

#s = 'bcbc'
#s1 = s [::-1]
#print (s)
#print (s1)
#print (s.translate({ord('b'):None}))


#condition
#s == s [::-1]
#s = "thisword"
#b = s.translate({ord(s[0]):None})
#print (s , b)

s = "aaab"
b = s.replace (s[0], '' ,1)
print (s , b)

def palindromeIndex(s):
    #print (len (s))
    if s == s [::-1]:
        return -1
        print ("already there")
    else:
        for i in range (len (s)) :
            if s.replace (s[i] , '' , 1) == s.replace (s[i] , '' , 1) [::-1]:
                #print (s.replace (s[i] , '' , 1) , s.replace (s[i] , '' , 1) [::-1])
                return i

            else:
                continue


    # Write your code here

s = 'aaab'
s = 'bcbc'
s = 'aaab'
s = "tpqknkmbgasitnwqrqasvolmevkasccsakvemlosaqrqwntisagbmknkqpt"
s_list = '''quyjjdcgsvvsgcdjjyq
hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh
fgnfnidynhxebxxxfmxixhsruldhsaobhlcggchboashdlurshxixmfxxxbexhnydinfngf
bsyhvwfuesumsehmytqioswvpcbxyolapfywdxeacyuruybhbwxjmrrmjxwbhbyuruycaexdwyfpaloyxbcpwsoiqtymhesmuseufwvhysb
fvyqxqxynewuebtcuqdwyetyqqisappmunmnldmkttkmdlnmnumppasiqyteywdquctbeuwenyxqxqyvf
mmbiefhflbeckaecprwfgmqlydfroxrblulpasumubqhhbvlqpixvvxipqlvbhqbumusaplulbrxorfdylqmgfwrpceakceblfhfeibmm
tpqknkmbgasitnwqrqasvolmevkasccsakvemlosaqrqwntisagbmknkqpt
lhrxvssvxrhl
prcoitfiptvcxrvoalqmfpnqyhrubxspplrftomfehbbhefmotfrlppsxburhyqnpfmqlaorxcvtpiftiocrp
kjowoemiduaaxasnqghxbxkiccikxbxhgqnsaxaaudimeowojk
'''.split()
print (s_list)
print (s == s [::-1])
for s in s_list :
    print (s , palindromeIndex(s))
#print ("palindromeIndex" , palindromeIndex(s))
