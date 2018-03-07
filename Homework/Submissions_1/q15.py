"""
Rock, Paper, Scissors, Lizard, Spock.
In this exercise, you are going to practice using conditionals (if, elif, else). You will write a small program that will determine the result of a Rock, Paper, Scissors, Lizard, Spock game.
For the rules of the game, please which the following clip from “The Big Bang Theory”:
https://www.youtube.com/watch?v=_PUEoDYpUyQ
The problem:
• Write a program that will first request the input for Player 1 and Player 2’s choices.
• Next, the program will print out the result (i.e., who the winner is).
S > P
P > R
R > S

R > L
L > Sp
Sp > S
S > L
L > P
P > Sp
Sp > R
R > S
"""

def get_winner(m1, m2):
    m1 = str(m1)
    m2 = str(m2)
    moves = ['R', 'P', 'S', 'L', 'Sp']
    players = ['Player 1', 'Player 2']
    winner = ''

    if m1 in moves and m2 in moves:
        if m1 == 'S' and m2 == 'P':
            winner = str(players[0])
        elif m1 == 'P' and m2 == 'R':
            winner = str(players[0])
        elif m1 == 'R' and m2 == 'S':
            winner = str(players[0])
        elif m1 == 'R' and m2 == 'L':
            winner = str(players[0])
        elif m1 == 'L' and m2 == 'Sp':
            winner = str(players[0])
        elif m1 == 'Sp' and m2 == 'S':
            winner = str(players[0])
        elif m1 == 'S' and m2 == 'L':
            winner = str(players[0])
        elif m1 == 'L' and m2 == 'P':
            winner = str(players[0])
        elif m1 == 'P' and m2 == 'Sp':
            winner = str(players[0])
        elif m1 == 'Sp' and m2 == 'R':
            winner = str(players[0])
        elif m1 == 'R' and m2 == 'S':
            winner = str(players[0])

        if m2 == 'S' and m1 == 'P':
            winner = str(players[1])
        elif m2 == 'P' and m1 == 'R':
            winner = str(players[1])
        elif m2 == 'R' and m1 == 'S':
            winner = str(players[1])
        elif m2 == 'R' and m1 == 'L':
            winner = str(players[1])
        elif m2 == 'L' and m1 == 'Sp':
            winner = str(players[1])
        elif m2 == 'Sp' and m1 == 'S':
            winner = str(players[1])
        elif m2 == 'S' and m1 == 'L':
            winner = str(players[1])
        elif m2 == 'L' and m1 == 'P':
            winner = str(players[1])
        elif m2 == 'P' and m1 == 'Sp':
            winner = str(players[1])
        elif m2 == 'Sp' and m1 == 'R':
            winner = str(players[1])
        elif m2 == 'R' and m1 == 'S':
            winner = str(players[1])

        statement = winner + ' wins!'

        print (statement)
    else:
        print ('Play appropriate move')

while True:
    m1 = input('Player 1? ')
    m2 = input('Player 2? ')
    get_winner(m1, m2)
    print ()
