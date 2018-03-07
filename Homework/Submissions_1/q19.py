"""
Significant figure calculator.
Your program should request in number input (i.e., either int or float) from the user, as well as the number of significant figures desired, and then output the first value input rounded to the number of significant figures specified.
The problem:
• Request a number from the user.
• Request the number of significant figures desired.
• Print out the first input corrected to the number of significant figures specified.
"""

number = float(input('Enter number: '))
sigfig = int(input('Enter significant figures: '))

def get_sigfig(number, sigfig):
    
