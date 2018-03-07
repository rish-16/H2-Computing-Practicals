"""
Caesar cipher.
The goal of this exercise is to write a cyclic cipher to encrypt messages. This type of cipher was used by Julius Caesar to communicate with his generals. It is very simple to generate but it can actually be easily broken and does not provide the security one would hope for.
The key idea behind the Caesar cipher is to replace each letter by a letter some fixed number of positions down the alphabet. For example, if we want to create a cipher shifting by 3, you will get the following mapping:
• Plain: ABCDEFGHIJKLMNOPQRSTUVWXYZ
• Cipher: DEFGHIJKLMNOPQRSTUVWXYZABC
To be able to generate the cipher above, we need to understand a little bit about how text is represented inside the computer. Each character has a numerical value and one of the standard encodings is ASCII (American Standard Code for Information Interchange). It is a mapping between the numerical value and the character graphic. For example, the ASCII value of ’A’ is 65 and the ASCII value of ’a’ is 97. To convert between the ASCII code and the character value in Python, you can use the following code:
                         letter = ’a’
                         # converts a letter to ascii code
                         ascii_code = ord(letter)
                         # converts ascii code to a letter
                         letter_res = chr(ascii_code)
                         print ascii_code, letter_res
The problem:
• Create a file called cipher.py. Start your program by asking the user for a phrase to encode
and the shift value. Then begin the structure of your program by entering in this loop (we’ll build on it more in a bit):
                         encoded_phrase = ’’
                         for c in phrase:
encoded_phrase = encoded_phrase + c
What does this loop do? Make sure you understand what the code does before moving on!
• Now modify the program above to replace all the alphabetic characters with ’x’. For example:
Enter sentence to encrypt: Mayday! Mayday! Enter shift value: 4
The encoded phrase is: Xxxxxx! Xxxxxx!
We are going to apply the cipher only to the alphabetic characters and we will ignore the others.
• Now modify your code, so that it produces the encoded string using the cyclic cipher with the shift value entered by the user. Let’s see how one might do a cyclic shift. Let’s say we have the sequence: 012345
If we use a shift value of 4 and just shift all the numbers, the result will be: 456789
• We want the values of the numbers to remain between 0 and 5. To do this we will use the modulus operator. The expression x % y will return a number in the range 0 to y - 1 inclusive, e.g., 4 % 6 = 4, 6 % 6 = 0, 7 % 6 = 1. Thus the result of the operation will be:
450123
Hint: Note that the ASCII value of ’A’ is 65 and ’a’ is 97, not 0. So you will have to think how to use the modulus operator to achieve the desired result. Apply the cipher separately to the upper and lower case letters.
"""
