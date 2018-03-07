def P(a, b):
    if b == 1:
        product = a
    elif b == 0:
        product = 0
    else:
        product = a + P(a, b-1)
    return product

p = P(20,20)
print (p)
