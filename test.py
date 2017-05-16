# def test(n):
#     for i in range(n):
#         print(i, "\t" , n)
#     return
#
# test(10)

# def triangulation(n):
#     j = 0
#     k = 0
#     for i in range(n):
#         j = i + 1
#         k = k + j
#         print str(j) + '\t' + str(k)
#
#     return
#
# triangulation(5)

# def sum_of_squares(list):
#     sums = 0
#     for i in list:
#         sums = sums + i**2
#
#     return sums
#
# print(sum_of_squares([2, -3, 4]))
# print(sum_of_squares([ ]))
# print(sum_of_squares([2, -3, 4]))

#def pointsCoveredSorted(l):
#    i = 0
#    R = []
#    while i<len(l):
#        s = l[i]
#        r = l[i]+1
#        j = i
#        i = i + 1
#        while i < len(l) and l[i]<=r:
#            i = i + 1
#            t = l[j:i]
#        R.append(t)
#        #R[i] = t
#    return R


#print pointsCoveredSorted([5,5.5,5.8,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5])

def linearsearch(l, item):
    pos = 0
    found = False
    stop = False
    while pos < len(l) and not found and not stop:
        if l[pos] == item:
            found = True
            print pos
        else:
            if l[pos] > item:
                stop = True
            else:
                pos = pos+1
    return pos,found

print linearsearch([1,3,4,5,7,9,10],8)




