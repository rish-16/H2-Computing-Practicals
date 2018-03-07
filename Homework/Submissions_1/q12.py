"""
Entering and printing your name.
The goal of this programming exercise is simply to get you more comfortable with using IDLE, and to begin using simple elements of Python. Standard elements of a program include the ability to print out results (using the print function), the ability to read input from a user at the console (e.g., using the input function), and the ability to store values in a variable, so that the program can access that value as needed.
The problem:
• Ask the user to enter his/her last name.
• Ask the user to enter his/her first name.
• Print out the user’s last and first names in that order.
"""

last = input('Enter your last name:\n')
first = input('Enter your first name:\n')
print ('{}\n{}'.format(last, first))
