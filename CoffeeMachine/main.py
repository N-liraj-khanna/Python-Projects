from menu import MENU
from menu import resources


def report():
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}"
          f"\nCoffee: {resources['coffee']}\nMoney: ${resources['money']}")


def get_money(coffee):
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    money_calc = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    change_calc = round(money_calc - MENU[coffee]['cost'], 2)
    resources['money'] += round(money_calc - change_calc, 2)
    return change_calc


def resources_check(coffee):
    water = MENU[coffee]['ingredients']['water']
    coffee_need = MENU[coffee]['ingredients']['coffee']
    if coffee != 'espresso':
        milk = MENU[coffee]['ingredients']['milk']

    if resources['water'] < water:
        return 'water'
    elif resources['coffee'] < coffee_need:
        return 'coffee'
    elif coffee != 'espresso' and resources['milk'] < milk:
        return 'milk'
    else:
        resources['water'] -= water
        resources['coffee'] -= coffee_need
        if coffee != 'espresso':
            resources['milk'] -= milk
        return 'Done'


on_machine = True

while on_machine:
    want = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()
    if want == "report":
        report()
    elif want == "off":
        on_machine = False
    else:
        change = get_money(want)
        if change < 0:
            print("Sorry that's not enough money. Money refunded.")
        else:
            res = resources_check(want)
            if res == 'Done':
                print(f"Here is ${change} in change.")
                print(f"Here is your {want} ☕️. Enjoy!")
            else:
                print(f"We don't have enough {res}! Sorry")

# TODO: "Ask if the person wants a coffee, continuously, until they input "off"
#  (coffee_machine)"
# TODO: "create a function report, and call it from coffee machine if the person
#  enters "report", make sure to initialize some random values, also, in the coffee
#  machine, initialize the prize of each coffee, and the required products to make em"
# TODO: "when a person asks for coffee, prompt them with the money(coffee machine)
#  calculate the money given, and compare em with the prize it is, if prize amount
#  is larger start making the coffee(and give back the balance)"
# TODO: "if smaller return with money input is less, now check for the ingredients
#  to make the coffee if larger, make the coffee and return back the change, if less
#  than tell em what product is missing"
