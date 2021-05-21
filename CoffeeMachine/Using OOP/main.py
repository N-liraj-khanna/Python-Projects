from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    drink_name = input(f"What would you like {menu.get_items()}report/off: ").lower()
    if drink_name == "off":
        is_on = False
    elif drink_name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        curr_order = menu.find_drink(drink_name)

        if coffee_maker.is_resource_sufficient(curr_order) and money_machine.make_payment(
                menu.find_drink(drink_name).cost):
            coffee_maker.make_coffee(curr_order)
