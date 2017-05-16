def palindrome(str):

    if len(str)==1:
        return str[0]
    else:
        return str[-1] + palindrome(str[:-1])

def ispal(str):
    str = str.replace(" ","")
    print str
    s = palindrome(str)
    if s == str:
        return True
    else:
        return False

print ispal("madam I m adam")