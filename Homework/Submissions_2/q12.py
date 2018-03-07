def minval(l):
    for j in range(len(l)-1,0,-1):
        for i in range(j):
            if l[i] > l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp


    minnum = l[0]

    return minnum

m = minval([54,26,93,17,77,31,44,55,20])
print (m)
