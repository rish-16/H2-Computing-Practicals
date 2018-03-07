"""
Birthdays and Zeller’s algorithm.
Zeller’s algorithm computes the day of the week on which a given date will fall (or fell). Use the description of Zeller’s algorithm, given below, to write a Python script that computes the day of the week on which the user’s birthday fell in the year they were born and prints the result to the screen.
Zeller’s algorithm:
• We first define the following variables (which each stores a non-negative integer):
month
This variable corresponds to the month of the year (ranging from 3 to 14), with March having the value 3, April the value 4, ..., December the value 12, and January and February (of the following year) being counted as months 13 and 14.
year
This variable corresponds to the year of the century (e.g., year = 89 for the year 1989; year = 5 for the year 2005). Note that if A == 13 or A == 14, then you should adjust C such that C = C - 1.

yy
This variable corresponds to the last 2 digits of year. For examples, yy == 89 for the year 1989 and yy == 5 for the year 2005.
century
This variable corresponds to the first 2 digits of year. For examples, century == 19 for the year 1989 and century == 20 for the year 2005.

day

This variable corresponds to the day of the month, i.e., an integer values between 1 and 31.
• The day of the week is then calculated using the following formula:
[day + ⌊13(month+1)⌋ + yy + ⌊yy⌋ + ⌊century⌋ − 2 × century] mod 7
• To determine the actual day of the week, the resultant value is then determined by referring to the following table:
   544
Resultant Value

Day of the Week

0
Saturday

1
Sunday

2

Monday
3
Tuesday
4
Wednesday

5
Thursday

6

Friday
The problem:
• Have the user input their birth date.
• Use Zeller’s algorithm to compute the day of the week on which they were born.
• Print out that day.

"""
