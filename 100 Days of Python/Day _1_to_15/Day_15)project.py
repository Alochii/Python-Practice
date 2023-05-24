import Day_15_menu as Menu


# TOD : print status
def report():
    # prints report status of all the resources available.
    print(f"""
    water : {Menu.resources["water"]}
    milk : {Menu.resources["milk"]}
    coffee : {Menu.resources["coffee"]}
    money available : {Menu.resources["money"]}
    """
          )


def check_drink(drink):
    water = Menu.MENU[drink]["ingredients"]["water"]
    milk = Menu.MENU[drink]["ingredients"]["milk"]
    coffee = Menu.MENU[drink]["ingredients"]["coffee"]
    machine_water = Menu.resources["water"]
    machine_milk = Menu.resources["milk"]
    machine_coffee = Menu.resources["coffee"]
    if machine_water - water < 0 or machine_milk - milk < 0 or machine_coffee - coffee < 0:
        print("you can't make this")
    else:
        print("you can make this drink")
        check_money(drink)


# TOD : read money and check if it matches the price.
def check_money(drink):
    price = Menu.MENU[drink]["cost"]
    print(f"insert money into the machine. your beverage costs ${price}")
    quarter = int(input("- Quarters ($0.25) : "))
    dime = int(input("- Dimes ($0.10) : "))
    nickle = int(input("- Nickels ($0.05) : "))
    penny = int(input("- Pennies ($0.01) : "))
    total_input = round((quarter * 0.25) + (dime * 0.1) + (nickle * 0.05) + (penny * 0.01), 2)
    print(total_input)
    if total_input < price:
        print(f"not enough money, the machine will return ${total_input}")
    else:
        print("enough money")
        buy_drink(price, total_input)
        update_resources(drink)
        print(f"Enjoy your {drink}!")


# TOD : tell the user what drink he got.

# TOD : return rest of money after dispensing the beverage.
def buy_drink(price, total_input):
    rest = round((total_input - price), 2)
    Menu.resources["money"] += price
    print(f"The machine will return ${rest} to you.")


def update_resources(drink):
    water = Menu.MENU[drink]["ingredients"]["water"]
    milk = Menu.MENU[drink]["ingredients"]["milk"]
    coffee = Menu.MENU[drink]["ingredients"]["coffee"]
    Menu.resources["water"] -= water
    Menu.resources["milk"] -= milk
    Menu.resources["coffee"] -= coffee


def main():
    while True:
        # print(Menu.MENU["espresso"]["ingredients"])
        choice = ""
        choice_list = ["espresso", "latte", "cappuccino", "report", "off"]
        while choice not in choice_list:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        print(choice)
        # TOD : report button to print how many resources we have
        if choice == "report":
            report()
        # TOD : read what beverage we want with a function that returns the amounts of resources needed.
        # TOD : button to turn off the machine for maintenance.
        elif choice == "off":
            break
        else:
            check_drink(choice)
    print("The machine will turn off now.")


main()
