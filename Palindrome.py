
def malayalam(w):
    #w = "malayalam"
    n = ""
    for i in range(len(w)-1,-1,-1):
        n = n + w[i]

    if n == w :
        print "its a palindrome"

    return n
print malayalam("1234321")



# def reverse(mystr):
#     reversed = ''
#     for char in mystr:
#         reversed = char + reversed
#
#     if reversed == mystr:
#          print "palindrome"
#
#     return reversed