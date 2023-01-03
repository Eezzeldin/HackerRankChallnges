'''
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
'''


n = 3


def create_cipher (n):
    cipher = {}
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
    "R","S","T","U","V","W","X","Y","Z"]
    letters_2 = [letters [letters.index(i) + n] for i in letters [:-n]]
    letters_3 = [letters [i] for i in range (len (letters [-n:]))]
    letters_4 = letters_2 + letters_3
    for i,j in zip (letters, letters_4): cipher [i] = j
    return cipher

def cipher_word (word,cipher):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
    "R","S","T","U","V","W","X","Y","Z"]
    encoded = ""
    #word    = "abcdefghij-klmnopq-rstuvwxyz"
    for w in word :
        if w.upper() in letters:
            #print (cipher [w.upper()])

            if w.islower ():
                encoded = encoded + cipher [w.upper()].lower()
            else:
                encoded = encoded + cipher [w.upper()]
        else:
            encoded = encoded + w
    return encoded


cipher      = create_cipher (3)
test_word_1 = "abcdefghij-klmnopq-rstuvwxyz"
test_word_2 = "There's-a-starman-in-the-sky"
print (cipher_word (test_word_1,cipher))
print (cipher_word (test_word_2,cipher))
