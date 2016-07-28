def  srApproximation(approx):
    half = approx/2
    betterapprox = 0.5 * (half + approx / half)
    count = 0
    while betterapprox != half:
        print betterapprox, half
        half = betterapprox
        betterapprox = 0.5 * (half + approx / half)
        count = count + 1

    return betterapprox,count

print(srApproximation(100))