def fib(n):
    a = 0
    b = 1
    for i in range(n):
        print a
        a,b = b, b + a

print fib(10)