import art
import os
clear = lambda: os.system('clear')

participants = {}
restart = True

print(art.logo)

print('Welcome to the auction program')

def count_the_biggest_bid():
    bid = 0
    winner = ''

    for participant in participants:
        if participants[participant] > bid:
            winner = participant
            bid = participants[participant]
    
    print(f'The winner is {winner}! \nBid: {bid}')

while restart:
    participant = str(input('What is your name?\n'))
    bid = int(input('What is your bid?\n'))
    participants[participant] = bid
    another_participants_exist = str(input('Are there any other bidders? (y / n)\n'))
    restart = another_participants_exist == 'y'
    
    if restart:
        clear()

count_the_biggest_bid()