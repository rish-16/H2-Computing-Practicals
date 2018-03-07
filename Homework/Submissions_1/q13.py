"""
Printing out multiplication tables.
Your program should request in integer input, between 1 and 12 (inclusive), from the user, and then output the multiplication table for that output (calculating the 1st to 12th multiple of that input number).
The problem:
• Request an integer input from the user (between 1 and 12 inclusive).
Let us denote this input as i.
• Print out the products of i * k, such that k=1,...,12.
"""

i = int(input('Enter number: '))

for k in range(1, 13):
    print (i * k)
