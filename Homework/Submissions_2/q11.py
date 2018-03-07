def mean(l):
    s = 0
    for i in l:
        s = s + i

    n = len(l)
    m = float(s / n)

    return m

m = mean([1,2,3,4,5,6,7])
print (m)
