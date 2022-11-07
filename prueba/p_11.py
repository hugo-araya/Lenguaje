a=2 
b=1 
c=3
if a > b:
    if a > c:
        if b > c:
            print (a, b, c)
        else:
            print (a, c, b)
    print (c, a, b)
else:
    if b > c:
        if a > b:
            print (b, a, c)
        else:
            print (b, c, a)
    print (c, b, a)