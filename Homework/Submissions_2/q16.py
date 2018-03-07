def powerset(s):
    sets = []
    sets.append([])
    sets.append(s)
    n = len(s)

    for i in range(n):
        sets.append([s[i]])

    return sets

sets = powerset([1,2,3])
print (sets)
