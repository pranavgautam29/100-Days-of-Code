import profile
from tkinter import Menu


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
}
profit = 0
def sufficient_resources(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry, not enough {item}")
            return False
        return True
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?"))*0.25
    total += int(input("how many dimes?"))*0.1
    total += int(input("how many nickles?"))*0.05
    total += int(input("how many pennies?"))*0.01
    return total

def transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost , 2)
        print(f"Here is ${change}, in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, thats not enough money. Money refunded.")
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")
is_on = True
while is_on:
    user_choice = input("What would you like? (latte/espreso/cappuccino):").lower()
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if sufficient_resources(drink["ingredients"]):
            payment = process_coins()
            transaction(payment , drink['cost'])
            make_coffee(user_choice , drink["ingredients"])





