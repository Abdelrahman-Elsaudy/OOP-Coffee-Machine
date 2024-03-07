from menu import MENU

stock = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


class Process:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0
        }
        self.beverage_list = [beverage for beverage in MENU]
        self.make_beverage = None

    def check_menu(self, beverage):
        if beverage not in self.beverage_list:
            print("Wrong input, item is not in menu.")
            return False
        else:
            return True

    def check_resources(self, beverage):
        self.make_beverage = True
        for item in stock:
            if item != "money":
                if self.resources[item] < MENU[beverage]["ingredients"][item]:
                    print(f"Sorry there isn't enough {item}.")
                    self.make_beverage = False
        return self.make_beverage

    def brewing(self, beverage):
        for item in stock:
            if item == "money":
                self.resources[item] += MENU[beverage]["cost"]
            else:
                self.resources[item] -= MENU[beverage]["ingredients"][item]

    def report(self):
        print(self.resources)
