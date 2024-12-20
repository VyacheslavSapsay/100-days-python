import random
import os
from art import logo


clear = lambda: os.system('clear')
levels = { 'easy': 10, 'hard': 5 }
restart = True

print('Welcome to Guess the Number game')

def compare_numbers(user_number):
    if user_number != number:
        if user_number > number:
            print('Too high. Try again')
        elif user_number < number:
            print('Too low. Try again')
        print(f'You have {attemps} attemps left')

while restart:
    level = ''

    clear()

    print(logo)

    while not level in levels:
        level = input('Choose the level - easy / hard:\n')

    attemps = levels[level]

    number = random.randint(0, 100)

    user_number = ''
    while user_number != number and attemps > 0:
        user_number = int(input('Guess the number:\n'))
        attemps -= 1
        compare_numbers(user_number)

    if user_number == number:
        print(f'You win. Choosen number is {number}')
    else:
        print(f'You loose. Choosen number is {number}')
    
    restart = input('Play again? (y/n):\n') == 'y'
