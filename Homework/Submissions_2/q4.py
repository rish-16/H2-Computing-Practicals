def power(x, n):
    if n == 0:
        answer = 1
    elif n == 0:
        answer = x
    else:
        answer = x * power(x,n-1)

    return answer

a = power(3,5)
print (a)
