"""
What is the output for each of the following pieces of code? Note: if the code does not terminate, write infinite loop.
i. a=0
while a < 3:
                     while True:
                         print(“X”, end = “”)
                         break
                     print(“O”, end = “”)
a=a+1 print(“”)
ii. a=1
while a < 3:
                     while a < 3:
                         print(“O”, end  = “”)
a=a+1 print(“”)
iii. a=1
while a < 3:
if a % 2 == 0: b=1
while b < 3:
print(“X”, end = “”) b=b+1
                     print(“O”, end = “”)
a=a+1 print(“”)

ANSWER:

1. XOXOXO
2. infinite loop
3. OXXO
"""
