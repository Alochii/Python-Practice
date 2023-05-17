from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
options = menu.get_items()

while True:
    choice = input(f"what drink would you like to have? ({options})")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        break
    else:
        drink = (menu.find_drink(choice))
        print(drink)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
