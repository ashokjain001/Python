def isPrime(n):
    for i in range(2, n):
        print n,i
        if n % i == 0:
            #print n,i
            return False
    return True

# print(isPrime(53))

def primelist(lists):
    test = []
    for i in lists:
        if isPrime(i):
            test.append(i)
    return test


lists = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1516, 17, 18]

print primelist(lists)
