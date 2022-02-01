from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else :
        drink = menu.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            # checks if the machine has enough resources to make the coffee entered by user
            if money_machine.make_payment(drink.cost) :
                #  if there are sufficient resources the machine will make the coffee and ask for payment
                # if user gave sufficient money code will return True, else False
                coffee_maker.make_coffee(drink)
                # machine will make coffee