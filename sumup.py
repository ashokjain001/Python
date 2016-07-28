def sumup(n):
    x = 0
    for i in range(1,n+1):
        x = x + i
    return x

n  = int(input("enter the no of integer to be summed"))

print sumup(n)