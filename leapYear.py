def isLeap(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 <> 0 and year % 4 == 0:
        return True
    else:
        return False

print isLeap(1986)
print isLeap(1944)
print isLeap(2011)
print isLeap(1800)
print isLeap(1900)
print isLeap(2000)
print isLeap(2056)

