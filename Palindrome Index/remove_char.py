'''
remove a charachter from a string
'''

s                 = "aabbcc"
remove_char_index = 3
print (s [remove_char_index])

first_half        = s [:remove_char_index]
print (first_half)

second_half       = s [remove_char_index+1:]
print (second_half)

s_trans           = first_half + second_half
print (s_trans)
