MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_resources(resources, menu, drink):
    """Takes the drink to prepare and return if there is enough resources to make the drink, return a list, this
    function also subtract the amount of water, milk and coffee from the resources for the chosen drink"""
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']

    drink_water = menu[drink]['ingredients']['water']
    drink_milk = menu[drink]['ingredients']['milk'] if drink != 'espresso' else None
    drink_coffee = menu[drink]['ingredients']['coffee']

    if drink == "espresso":
        if water >= drink_water and coffee >= drink_coffee:
            resources['water'] -= drink_water
            resources['coffee'] -= drink_coffee
            return [True]
        else:
            return [
                False,
                '' if water >= drink_water else 'water',
                '' if coffee >= drink_coffee else 'coffee'
            ]
    else:
        if water >= drink_water and milk >= drink_milk and coffee >= drink_coffee:
            resources['water'] -= drink_water
            resources['milk'] -= drink_milk
            resources['coffee'] -= drink_coffee
            return [True]
        else:
            return [
                False,
                '' if water >= drink_water else 'water',
                '' if milk >= drink_milk else 'milk',
                '' if coffee >= drink_coffee else 'coffee'
            ]


def enough_money(Q, D, N, P, menu, drink):
    """This function make the calculation to add the money to the resources when it is enough, if not return a list with a
    boolean and a message for the user"""
    user_quarters = 0.25 * Q
    user_dimes = 0.10 * D
    user_nickels = 0.05 * N
    user_pennies = 0.01 * P

    total = user_quarters + user_dimes + user_nickels + user_pennies

    if total >= menu[drink]['cost']:
        change = total - menu[drink]['cost']
        resources['money'] += (total - change)
        if change != 0:
            return [True, f"You change is ${change}."]
        else:
            return [True]
    else:
        return [False, "Sorry but there is not enough money to buy a coffee."]


def coffee_machine():
    end = False
    prompt = input("What would you like? (espresso/latte/cappuccino): ")

    if prompt == "report":
        print(f"Water: {resources['water']}ml.\nMilk: {resources['milk']}ml.\nCoffee: {resources['coffee']}gr.\nMoney: ${resources['money']}")
        coffee_machine()
    elif prompt == "off":
        end = True
        return
    elif prompt == "espresso":
        enough = check_resources(resources=resources, menu=MENU, drink=prompt)
    elif prompt == "latte":
        enough = check_resources(resources=resources, menu=MENU, drink=prompt)
    elif prompt == "cappuccino":
        enough = check_resources(resources=resources, menu=MENU, drink=prompt)
    else:
        print("Wrong command. I coffee machine don't know what to do, Try again please.")
        coffee_machine()


    if enough[0]:
        print("Insert the money. Only accepts coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))

        is_money_enough = enough_money(Q=quarters, D=dimes, N=nickels, P=pennies, menu=MENU, drink=prompt)
    else:
        for item in enough:
            if item == '' or item == False:
                continue
            else:
                print(f"Sorry there is not enough {item}.")
        return

    if is_money_enough[0]:
        if is_money_enough[1]:
            print(f"{is_money_enough[1]}")
            print(f"There is your {prompt}, Enjoy it.")
        else:
            print(f"There is your {prompt}, Enjoy it.")
    else:
        print(f"{is_money_enough[1]}")

    if end:
        return
    else:
        coffee_machine()


coffee_machine()