from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    user_choice = input(f'What would you like? {menu.get_items()}: ')

    if user_choice == 'off':
        is_on = False
        continue
    elif user_choice == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        
        is_sufficient = coffe_maker.is_resource_sufficient(drink)

        if not is_sufficient:
            continue

        if money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)



        


    


