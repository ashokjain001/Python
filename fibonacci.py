
# def fibb(n):
#     if n <= 1:
#         return n
#     else:
#         return fibb(n-2)+fibb(n-1)
#
# print fibb(40)
# #

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

def fibb(n):
    fib = []
    fib.insert(0,0)
    fib.insert(1,1)
    count = 0
    for i in range(2,n+1):
        fib.insert(i,(fib[i-1]+fib[i-2]))
        count = count + 1
    return fib, count+1

input = int(input("Enter number to compute fibbonacci series "))

print fibb(input)


