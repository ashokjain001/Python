import time

#list concatination
def list():
    l = []
    start = time.time()
    for i in range(1000):
        l = l + [i]
    end = time.time()
    return end - start

#apped is faster than cancat
def list2():
    l = []
    start = time.time()
    for i in range(1000):
        l.append(i)
    end = time.time()
    return end - start

# list comprehension faster than concatination and append
def list3():
    l = []
    start = time.time()
    l = [i for i in range(1000)]
    end = time.time()
    return end - start

def list4():
    l = []
    start = time.time()
    l = list(range(1000))
    end = time.time()
    return end - start

def testrun():
    for i in range(5):
        print list4()

print testrun()
