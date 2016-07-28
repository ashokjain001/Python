import random
def max_pair(lis):
    maxi= 0
    for i in range(len(lis)):
        for j in range(len(lis)):
            if(i!=j):
                mult = lis[i]*lis[j]
                if mult>maxi:
                    maxi = mult
    return maxi

#print max_pair([5,100000,7,3,4,8,90000])

def max_pair_fast(lis):
    maxi = 0
    maxpos = 0
    maxi2 = 0
    for i in range(len(lis)):
        if lis[i] > maxi:
            maxi = lis[i]
            maxpos = i

    for i in range(len(lis)):
        if i != maxpos:
            if lis[i] > maxi2:
                maxi2 = lis[i]

    return maxi * maxi2

def stressTest():
    lis = []
    for j in range(100):
        for i in range(100):
            num = random.randrange(0, 100000)
            lis.append(num)
        print lis
        a = max_pair(lis)
        b = max_pair_fast(lis)
        if a == b:
            print (a,b,"same outout")
        else:
            print (a,b,"different outout")
        del lis[:]
print stressTest()

# print max_pair([34, 5, 6, 40, 3, 2, 8, 7, 40])
# print max_pair_fast([34, 5, 6, 40, 3, 2, 8, 7, 40])
#
