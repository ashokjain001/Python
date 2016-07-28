# def vowel(x):
#     vow = "aeiouAEIOU"
#     newword = ""
#     for i in x:
#         if i not in vow:
#             newword = newword + i
#     return newword
#
#
# print vowel("ashok")
# import turtle
#
# def applyrules(input):
#     if input == "F":
#         return "F-F++F-F"
#     else:
#         return input
#
# def stringprocessing(input):
#     str = ""
#     for chr in input:
#       str = str + applyrules(chr)
#     return str
#
# def createlsystem(input,n):
#     i = 0
#     endString = ""
#     while i <=n:
#         i = i + 1
#         endString  = stringprocessing(input)
#         input = endString
#
#     return endString
#
# def drawLsystem(aTurtle, instructions, angle, distance):
#     for cmd in instructions:
#         if cmd == 'F':
#             aTurtle.forward(distance)
#         elif cmd == 'B':
#             aTurtle.backward(distance)
#         elif cmd == '+':
#             aTurtle.right(angle)
#         elif cmd == '-':
#             aTurtle.left(angle)
#
# def main():
#     inst = createlsystem("F",3)
#     print inst
#     t = turtle.Turtle()
#     wn = turtle.Screen()
#     t.up()
#     t.back(350)
#     t.down()
#     t.speed(100)
#     drawLsystem(t,inst,60,8)
#     wn.exitonclick()
# print main()

# def count(str,letter):
#     i = 0
#     for j in str:
#         if j == letter:
#             i = i+1
#     return i
#
# print count("banana","a")

# prefixes = "JKLMNOPQ"
# suffix = "ack"
# ssuffix = "uack"
# for p in prefixes:
#   if (p != 'O') and (p != 'Q'):
#     print(p + suffix)
#   else:
#     print(p + ssuffix)

# var = """Fully furnished room with private bath is available in 2 Bed rooms 2 Bath apartment for male/female in Irving. washer dryer available in the unit. Rent is $600 Including utilities and high speed internet. Month to month option available, cooking allowed(veg/non-veg). Room is available only from July 1st. I would like to know something about yourself, your profession, education, why are you looking for room, is it for short stay or long stay, married or unmarried, stable income and id proof etc.. Address is W Walnut hill ln irving texas 75038, check whether its convenient for your commute and Email me at forrentirving at gmail to discuss and view the room. Prefer someone who is willing to stay 6 months."""
#
# j = 0
# for i in var:
#     if i == "e":
#         j = j+1
# print "your text contains %d alphabetic characters, of which %d(%d) are e" %(len(var),j,(j/len(var))*100)
# print ("your text contains",len(var)/len(var))

# for i  in range(1,13):
#     for j in range(1,13):
#         #print(i,"*",j,i*j)
#         print "%d*%d = %d"%(i,j,i*j)

# var = str(200)
# print type(len(var))
# print len(var)

# ashok = "python"
# a = ""
# for i in range(len(ashok)-1,-1,-1):
#     a = a + ashok[i]
# print ashok+a
#
# def reverse(mystr):
#     reversed = ''
#     for char in mystr:
#         reversed = char + reversed
#
#     if reversed == mystr:
#          print "palindrome"
#
#     return reversed
#
# # def mirror(mystr):
# #     return mystr + reverse(mystr)
#
# print reverse("ashok")
# def test(a,remove):
#     j = ""
#     for i in range(len(a)):
#         if a[i] != remove:
#             j = j + a[i]
#     return j
#
# print test("this is asho a a aj jjaj", "a")

# def pure(list):
#     n = []
#     for i in range(len(list)):
#         c = list[i] * 2
#         n.append(c)
#     return n
# print pure([1,2,4,56,3,2,98])

# def modifiers(list):
#     for i in range(len(list)):
#         list[i] = 2 * list[i]
#     return list
#
# things = [1,2,3,4,5]
# print things
# print modifiers(things)
# print things

# def list(lists):
#     #test = []
#     for i in range(len(lists)):
#         lists[i] = 3 * lists[i]
#         #test.append(n)
#     return lists
#
# things = [1,23,4,5,6,7,8,9]
# print things
# print list(things)
# print things


# def isPrime(list):
#     for i in list:
#         for j in range(i):
#             if i % j == 0:
#                 print "not a prime"
#             print "it is a prime"
#
# print isPrime([2,3,4,5,6,7,8])

# def recursive(n):
#     if n < 1:
#         return 1
#     else:
#         return n * recursive(n-1)
#
#
# print recursive(4)

# def reverse(s):
#     print s
#     if len(s) <= 1:
#         return s[0]
#     else:
#         return s[len(s)-1] + reverse(s[:len(s)-1])
# print reverse("ashok")


# def lis(lis):
#     maxi= 0
#     for i in range(len(lis)):
#         for j in range(len(lis)):
#             if(i!=j):
#                 mult = lis[i]*lis[j]
#                 if mult>maxi:
#                     maxi = mult
#     return maxi
#
# print lis([5,100000,7,3,4,8,90000])

# def max_pair(lis):
#     maxi = 0
#     maxpos = 0
#     maxi2 = 0
#     for i in range(len(lis)):
#         if lis[i] > maxi:
#             maxi = lis[i]
#             maxpos = i
#
#     for i in range(len(lis)):
#         if i != maxpos:
#             if lis[i] > maxi2:
#                 maxi2 = lis[i]
#
#     return maxi, maxi2, maxi * maxi2
# print max_pair([3,4,5,6,40,3,2,8,7,5])

# def fibb(n):
#     if n <= 1:
#         return n
#     else:
#         return fibb(n-2)+fibb(n-1)
#
# print fibb(50)

# def fibb(n):
#     num = 0
#     num1 = 1
#     sum = 0
#     for i in range(n):
#         sum = num + num1
#         num = num1
#         num1 = sum
#     return sum
#
# print fibb(10)


# def reverse(s):
#     print s[len(s)-1:]
#     if len(s)<=1:
#         return s[0]
#     else:
#         return s[len(s)-1] + reverse(s[:len(s)-1])
#
# print reverse("ashok")
#
#
# def rev(s):
#     r = ""
#     for i in range(len(s)):
#         r = s[i] + r
#     return r
#
# print rev("ashok")


# def smallest(l):
#     small = l[0]
#     for i in l:
#         is_small = True
#         for j in l:
#             if i>j:
#                 is_small = False
#         if is_small is True:
#             small = i
#     return small
# print smallest([4,2,3,6,7,8,1,2,0,5,6,23,-34,45,65,8])

# def test1(n):
#     l = []
#     for i in range(n):
#         l = l + [i]
#     return l
#
# print test1(1000)
#
# def test2():
#     l = list(range(1000))
#     return l
# print test2()

# def test3():
#     l = [i for i in range(1000)]
#     return l
# print test3()

# def search(l,n):
#     for i in range(len(l)):
#         if l[i] == n:
#             return i
#     return False
# print search([8,5,4,3,9,12,34,56,8,9],89)

# def common(a,b):
#     l = []
#     for i in a:
#         for j in b:
#             if i==j:
#                 l.append(i)
#     return l
#
# print common([8,5,4,3,9,12,34,56],[8,5,4,3,9,12,34,56])
#
# def insertion(l):
#     ll = len(l)
#     a = 0
#     for i in range(ll):
#         if l[a] > l[a+1]:
#             l.insert(a,l[a+1])
#         print l
#
# print insertion([8,5,4,3,9,12,34,56])

def fibb(n):
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2,n+1):
        fib.append((fib[i-2]+fib[i-1])mod 10)
    return fib
print fibb(40)

