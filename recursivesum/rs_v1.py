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
        if len ( str (super (p)) ) == 1:
            print (str (super (p)))
            return super (p)
        else:
            print (i)
            p = str (super (p))
            print (p)

    
