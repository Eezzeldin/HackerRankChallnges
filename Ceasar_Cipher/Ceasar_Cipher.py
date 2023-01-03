'''
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
'''

cipher = {}
n = 3

#abcdefghijklmnopqrstuvwxyz
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
"R","S","T","U","V","W","X","Y","Z"]
print (len (letters))

letters_2 = [letters [letters.index(i) + n] for i in letters [:-n]]
print (letters_2)

letters_3 = [letters [i] for i in range (len (letters [-n:]))]
print (letters_3)

letters_4 = letters_2 + letters_3
print (letters_4)

for i,j in zip (letters, letters_4): cipher [i] = j
print (cipher)


encoded = ""
word    = "abcdefghij-klmnopq-rstuvwxyz"
for w in word :
    if w.upper() in letters:
        print (cipher [w.upper()])

        if w.islower ():
            encoded = encoded + cipher [w.upper()].lower()
        else:
            encoded = encoded + cipher [w.upper()]
    else:
        encoded = encoded + w
print (encoded)


def cipher_word (word):
    encoded = ""
    #word    = "abcdefghij-klmnopq-rstuvwxyz"
    for w in word :
        if w.upper() in letters:
            print (cipher [w.upper()])

            if w.islower ():
                encoded = encoded + cipher [w.upper()].lower()
            else:
                encoded = encoded + cipher [w.upper()]
        else:
            encoded = encoded + w
    return encoded

test_word_1 = "abcdefghij-klmnopq-rstuvwxyz"
test_word_2 = "There's-a-starman-in-the-sky"
print (cipher_word (test_word_1))
print (cipher_word (test_word_2))
