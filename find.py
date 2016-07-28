def find(input, to_find, param):
    i = 0
    found = False
    while i <= len(input) and not found:
        if input[i] == to_find:
            found = True
        else:
            i = i + 1

    if found == True:
        return i
    else:
        return -1

print find("banana","n")