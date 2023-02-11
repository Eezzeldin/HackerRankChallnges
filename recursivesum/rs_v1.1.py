def super (p): return sum (list (map (int , sorted (p))))


def superDigit(n, k):
    # Write your code here

    #concaninae n k times
    p = ""
    for i in range (k):
        p = p+n
    iterations = 100
    print (p)
    for i in range (0,iterations):
        x = str (super (p))
        if len ( x ) == 1:
            #print (x)
            return int (x)
        else:
            #print (i)
            p = x
            #print (p)
