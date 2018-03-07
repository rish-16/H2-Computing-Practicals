"""
The following code loops infinitely when run, Fix the code so that its output is “OOOXOXOO”.

a=1
while a < 3:
b=1
while b < 3:
                     if a == 2:
                         print(“X”, end = “”)
print “O”,
b=b+1 print(“O”, end = “”)
print(“”)


"""

"""
a=1
while a < 3:
    b=1
    while b < 3:
        if a == 2:
            print("X", end = "")
        print ("O")
        b=b+1
    print("O", end = "")
"""

a = 1
while a < 3:
    b = 1
    while b < 3:
        if a == 2:
            print ("X", end="")
        print ("O", end="")
        b += 1
    a += 1
    print ("O", end="")
