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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True
quarters = 0.25
dimes = 0.1
nickels = 0.05
pennies = 0.01
change = 0
profit = 0


def check_resources(drink):
    if resources['water'] >= drink['ingredients']['water']:
        return True
    elif resources['milk'] >= drink['ingredients']['milk']:
        return True
    elif resources['coffee'] >= drink['ingredients']['coffee']:
        return True
    else:
        return False


def process_coins(quarter, dime, nickel, penny, ordered):
    quarters = int(input('how many quarters? '))
    dimes = int(input('how many dimes? '))
    nickels = int(input('how many nickels? '))
    pennies = int(input('how many pennies? '))

    quarter_amount = quarter * quarters
    dime_amount = dime * dimes
    nickel_amount = nickel * nickels
    penny_amount = penny * pennies
    payment = quarter_amount + dime_amount + nickel_amount + penny_amount

    drink_cost = MENU[ordered]['cost']

    if payment > drink_cost:
        change = payment - drink_cost
        print(f'Here is ${round(change, 2)} dollars in change.')
        return True
    elif payment < drink_cost:
        print('sorry, your payment is not enough, money refunded')
        global profit
        profit -= drink_cost
        return False


def make_coffee(order_ingredients, drink_name):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name}, Enjoy!')


while is_on:

    order = input('do you want an espresso, latte or cappuccino? ').lower()

    if order == 'off':
        is_on = False
    elif order == 'report':
        print(f"water: {resources['water']}ml,")
        print(f"milk: {resources['milk']}ml,")
        print(f"coffee: {resources['coffee']}g,")
        print(f"money: ${profit}")
    else:
        drink = MENU[order]
        if check_resources(drink):

            profit += drink['cost']
            print('Please insert coins.')
            if process_coins(quarters, dimes, nickels, pennies, order):
                make_coffee(drink['ingredients'], order)



