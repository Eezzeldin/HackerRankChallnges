def removechar (s,i):
    #removes char by index from string
    return s [:i] + s [i+1:]

def reversestring (s):
    return s [::-1]

def is_palindromeIndex(s):
    return s == reversestring (s)

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

            forward_s = removechar (s,forward_index)
            backward_s= removechar (s,backward_index)

            if is_palindromeIndex (forward_s):
                return forward_index
            elif is_palindromeIndex (backward_s):
                return backward_index


    return -1
