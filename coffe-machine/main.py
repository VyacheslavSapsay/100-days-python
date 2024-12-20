def off_the_machine():
    global should_continue
    should_continue = False

def print_report():
    for resource in resources:
        print(f'{resource}: {resources[resource]}')

def make_drink(drink_name):
    drink = drinks[drink_name]

    resources['money'] += drink['price']

    for resource in drink['resources']:
        resources[resource] -= drink['resources'][resource]
    
    print(f'Here is your {drink_name}! Enjoy ☕')

def check_if_drink_is_available(drink_name):
    drink_resources = drinks[drink_name]['resources']
    is_available = True

    for resource in resources:
        if resource in drink_resources:
            if resources[resource] < drink_resources[resource]:
                print(f'Sorry there is not enough {resource}.')
                is_available = False
                break
    return is_available

def check_if_enough_money_for_drink(money, drink):
    if money < drink['price']:
        print("Sorry, that's not enough money.  Money refunded.")
        return False
    elif money > drink['price']:
        change = money - drink['price']
        print(f'Here is ${change} in change')
        return True

def count_user_money():
    user_money = 0

    for coins in available_coins:
        coins_amount = int(input(f'How many {coins}?\n'))
        user_money += available_coins[coins] * coins_amount

    return user_money

if __name__ == "__main__":
    drinks = {
        'espresso': {
            'price': 1.5,
            'resources': {
                'water': 50,
                'coffee': 18,
                'milk': 0
            }
        },
        'latte': {
            'price': 2.5,
            'resources': {
                'water': 200,
                'coffee': 24,
                'milk': 150
            }
        },
        'cappuccino': {
            'price': 3.0,
            'resources': {
                'water': 250,
                'coffee': 24,
                'milk': 100
            }
        }, 
    }

    resources = {
        'water': 300,
        'milk': 200,
        'coffee': 100,
        'money': 0
    }

    available_coins = {
        'quarters': 0.25,
        'dimes': 0.10,
        'nickles': 0.05,
        'pennies': 0.01
    }

    commands = {'off': off_the_machine, 'report': print_report}

    should_continue = True

    def main():
        while should_continue:
            user_input = ''

            while user_input not in drinks and user_input not in commands:
                user_input = input(f'What would you like? {'/'.join(drinks.keys())}\n')
            
            if user_input in drinks:
                chosen_drink = drinks[user_input]
                is_drink_available = check_if_drink_is_available(user_input)

                if not is_drink_available:
                    continue

                user_money = count_user_money()

                is_money_enough = check_if_enough_money_for_drink(user_money, chosen_drink)

                if not is_money_enough:
                    continue

                make_drink(user_input)
            else:
                command = commands[user_input]
                command()
                continue

    main()