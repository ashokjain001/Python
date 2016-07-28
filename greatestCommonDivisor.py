# def gcd(a, b):
#     divisor = 0
#     for i in range(1, min(a, b)):
#         if (a % i == 0) and (b % i == 0):
#             divisor = i
#     return divisor
#
#
# print gcd(30, 20)


def gcd_euclidean(a,b):
    if b == 0:
        return a
    else:
        return gcd_euclidean(b,a%b)

print gcd_euclidean(357,234)
