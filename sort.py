def sort(lis):
    for i in range(len(lis)):
        for j in range(len(lis)):
             if lis[i]!=lis[j]:
                if lis[i] < lis[j]:
                    lis[i],lis[j] = lis[j],lis[i]
    return lis

print sort([6,9,3,8,4,2,8,9])




