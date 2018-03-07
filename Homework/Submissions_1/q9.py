"""
What is the output for each of the following pieces of code?
i. keep_going = True a=0
b=0
while keep_going:
print(“O”, end = “”) a=a+5
b=b+7
if a + b >= 24:
                         keep_going = False
                 print(“”)
ii. keep_going = True a=0
b=0
while keep_going:
                     print(“O” , end = “”)
                     if a + b >= 24:
keep_going = False a=a+5
b=b+7 print(“”)
iii. keep_going = True a=0
b=0
while keep_going:
print(“O” , end = “”)
a=a+5
b=b+7
ifa+b>24: #notethat“>”isusedhere...vs“>=”in(i)
                         keep_going = False
                 print(“”)
iv. keep_going = True a=0
b=0
while keep_going:
                     print(“O” , end = “”)
                     if a + b > 24:
keep_going = False # note that “>” is used here ... vs “>=” in (ii) a=a+5
b=b+7 print(“”)

ANSWER:

1. 00
2. 000
3. 000
4. 0000
"""

keep_going = True
a=0
b=0
while keep_going:
    print("0", end = "")
    if a + b > 24:
        keep_going = False
    a=a+5
    b=b+7
# print()
