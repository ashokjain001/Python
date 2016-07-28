def sequence(n):
    #print n
    x = 0
    y = 0
    while n != 1:
        x = x+1
        #print n
        if n % 2 == 0:
            n =  n // 2
        else:
            n = 3*n + 1
    print x," steps"
    return x

z = 0
maxSoFar = 0
for i in range(1,100):
    print (i," sequence")
    result = sequence(i)
    if result > 100:
        z = z + 1
    if result > maxSoFar :
        maxSoFar =  result


    print "More than 100 iterations",z, " and maximum is", maxSoFar



