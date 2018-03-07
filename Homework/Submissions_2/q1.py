def factorial(n):
    if n == 0:
        product = 0
    elif n == 1:
        product = 1
    else:
        product = n * factorial(n-1)

    return product

p = factorial(10)
print (p)
