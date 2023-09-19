from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()



while True :
    options = menu.get_items()
    choice = input(f"what would you like? ({options})")
    if choice == "off" :
        break
    elif choice == "report" :
        coffee_maker.report()
        money_machine.report()
    else :
        drink = menu.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink) :
            money_machine.make_payment(me)
