
# def lcm(a,b):
#     i = max(a,b)+1
#     while i%a <> 0 or i%b <> 0:
#         i = i + 1
#     return i
# print lcm(6,8)

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
print gcd(120,100)

def lcm2(a,b):
    return a*b/(gcd(a,b))

print lcm2(28851538,1183019)