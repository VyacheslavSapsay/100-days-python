import random
import os
import art

ACCOUNTS_TO_COMPARE_COUNT = 2

famous_instagram_accounts = [
    {'description': 'Instagram, a Social Media Platform', 'subscribers_count': 600000000},
    {'description': 'Cristiano Ronaldo, a Football player, from Portugal', 'subscribers_count': 598000000},
    {'description': 'Lionel Messi, a Football player, from Argentina', 'subscribers_count': 482000000},
    {'description': 'Kylie Jenner, a Reality TV Star and Entrepreneur, from United States', 'subscribers_count': 398000000},
    {'description': 'Selena Gomez, a Singer and Actress, from United States', 'subscribers_count': 420000000},
    {'description': 'Dwayne Johnson, an Actor and Former Wrestler, from United States', 'subscribers_count': 394000000},
    {'description': 'Ariana Grande, a Singer and Actress, from United States', 'subscribers_count': 377000000},
    {'description': 'Kim Kardashian, a Reality TV Star and Entrepreneur, from United States', 'subscribers_count': 364000000},
    {'description': 'Beyoncé, a Singer and Actress, from United States', 'subscribers_count': 308000000},
    {'description': 'Khloé Kardashian, a Reality TV Star, from United States', 'subscribers_count': 311000000},
    {'description': 'Justin Bieber, a Singer, from Canada', 'subscribers_count': 292000000},
    {'description': 'Kendall Jenner, a Model and Reality TV Star, from United States', 'subscribers_count': 283000000},
    {'description': 'Taylor Swift, a Singer and Songwriter, from United States', 'subscribers_count': 268000000},
    {'description': 'Neymar Jr., a Football player, from Brazil', 'subscribers_count': 211000000},
    {'description': 'Jennifer Lopez, a Singer and Actress, from United States', 'subscribers_count': 250000000},
    {'description': 'Nicki Minaj, a Rapper and Singer, from Trinidad and Tobago', 'subscribers_count': 210000000},
    {'description': 'Miley Cyrus, a Singer and Actress, from United States', 'subscribers_count': 220000000},
    {'description': 'Kourtney Kardashian, a Reality TV Star, from United States', 'subscribers_count': 210000000},
    {'description': 'Kevin Hart, a Comedian and Actor, from United States', 'subscribers_count': 150000000},
    {'description': 'LeBron James, a Basketball player, from United States', 'subscribers_count': 160000000}
]

clear = lambda: os.system('clear')

def game(user_score = 0, continue_the_game = False):
    clear()
    print(art.logo)
    if continue_the_game:
        print(f"You're right! Current score: {user_score}.")

    accounts_to_compare = get_accounts_for_comparison()

    print(f'Compare 1: {accounts_to_compare[0]['description']}')
    print(art.versus_logo)
    print(f'Compare 2: {accounts_to_compare[1]['description']}')

    right_answer = get_right_answer(accounts_to_compare)
    print(right_answer)
    user_answer = input('Who has more followers? Type 1 or 2:')

    check_user_answer(right_answer, user_answer, user_score)

def get_right_answer(accounts_to_compare):
    account_with_more_folowers = accounts_to_compare[0]

    for account in accounts_to_compare:
        if account['subscribers_count'] > account_with_more_folowers['subscribers_count']:
            account_with_more_folowers = account
    
    return str(accounts_to_compare.index(account_with_more_folowers) + 1)

def get_accounts_for_comparison():
    accounts_to_compare = [None] * ACCOUNTS_TO_COMPARE_COUNT

    for i in range(ACCOUNTS_TO_COMPARE_COUNT):
        accounts_to_compare[i] = random.choice(famous_instagram_accounts)

    while accounts_to_compare[0] == accounts_to_compare[1]:
        accounts_to_compare[0] = random.choice(famous_instagram_accounts)
    
    return accounts_to_compare

def check_user_answer(right_answer, user_answer, user_score):
    if user_answer != right_answer:
        print(f"Sorry, that's wrong. Final score: {user_score}")
    else:
        user_score += 1
        game(user_score = user_score, continue_the_game = True)

game()
