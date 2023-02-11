'''
STDIN   Function
-----   --------
3       q = 3
aaab    s = 'aaab' (first query)
baa     s = 'baa'  (second query)
aaa     s = 'aaa'  (third query)
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
    for i in range (len (s)) :
        if s.replace (s[i] , '' , 1) == s.replace (s[i] , '' , 1) [::-1]:
            return i
        else:
            continue
    if i == len (s):
        return -1

    # Write your code here

s = 'aaab'
s = 'bcbc'
s = 'aaab'
s = "quyjjdcgsvvsgcdjjyq"
print ("palindromeIndex" , palindromeIndex(s))
