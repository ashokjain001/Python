def anagram2(s1,s2):
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()

    if s1 == s2:
        return True
    else:
        return False

print anagram2('abcd','dcba')