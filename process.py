from menu import MENU

stock = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

beverage_list = [beverage for beverage in MENU]

class Process:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def check_menu(self, beverage):
        if beverage not in beverage_list:
            print("Wrong input, item is not in menu.")
        else:
            return True

    def check_resources(self, beverage):
        for item in stock:
            if item != "money":
                if self.resources[item] < MENU[beverage]["ingredients"][item]:
                    print(f"Sorry there isn't enough {item}.")
                    return False

    def brewing(self, beverage):
        for item in stock:
            if item != "money":
                self.resources[item] -= MENU[beverage]["ingredients"][item]

    def report(self):
        print(self.resources)