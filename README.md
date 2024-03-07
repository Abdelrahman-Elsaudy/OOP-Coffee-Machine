# OOP Coffee Machine

---

- This is the Object-Oriented Programming version, I wrote a traditional one in a separate repository.
- This program represents the software of a coffee machine that can make 3 types of drinks: espresso, cappuccino and latte.
- After you choose your beverage it checks to see if it has enough stock of ingredients to make it.
- If so, it asks you to insert money, gives you the change and serves you the drink ☕.
- You can order more drinks if it has enough resources.
- You can check the stock ingredients and money at any time by typing "report".
- You can turn off the machine by typing "off".
- The drinks, their ingredients and cost are written inside a variable called `MENU` as JSON format.

---
## Machine Logic Sequence.

1. Check if the order in menu
2. if so, check if the machine has enough resources to make the order
3. if so, asks the user to provide money
4. if they provide enough money, it gives the user the change, and the beverage is served 
(beverage ingredients are subtracted from the stock ingredients and beverage cost is added to the stock money).

---
## Applied Skills:

- Object-Oriented Programming
- Functions with inputs and outputs.
- Logical if statements.
- While loops.
- List comprehension.
- JSON format manipulation.

---

## Explaining The Project Using OOP:
Dividing the code into 4 coding pages:
- `menu.py` which contains the drinks, their ingredients and cost.
- `process.py` which contains the _Process_ class in which:
  - Attributes are the machine stock ingredients and money, and a function to print them when the user types "report".
```
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0
        }
        self.beverage_list = [beverage for beverage in MENU]
```
  - A function to check if the user input is in the `MENU`.
```
    def check_menu(self, beverage):
        if beverage not in self.beverage_list:
            print("Wrong input, item is not in menu.")
            return False
        else:
            return True
```
  - A function to check if the machine has enough stock of ingredients to make the beverage.
```
    def check_resources(self, beverage):
        self.make_beverage = True
        for item in stock:
            if item != "money":
                if self.resources[item] < MENU[beverage]["ingredients"][item]:
                    print(f"Sorry there isn't enough {item}.")
                    self.make_beverage = False
        return self.make_beverage
```
  - A function to make the beverage (subtract the beverage ingredients from the stock ingredients and add the beverage cost to the stock money).
Note: this function gets called after the machine checks that the user provided enough money (will be explained later).
```
    def brewing(self, beverage):
        for item in stock:
            if item == "money":
                self.resources[item] += MENU[beverage]["cost"]
            else:
                self.resources[item] -= MENU[beverage]["ingredients"][item]
```
- `money.py` which takes money as input in the form of quarters, dimes, nickles and pennies and checks if the provided money 
is enough to make the requested beverage.
```
    def checking(self, beverage):
        print("Please insert coins.")
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        total_in_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
        self.change = round(total_in_money - float(MENU[beverage]["cost"]), 2)
        if self.change < 0:  # which means the money entered is less than the cost of the beverage.
            print("Not enough money, money refunded.")
            return False
        else:
            return True
```
- `main.py` in which the machine is operating in a `while` loop to take the orders from the user. These lines are the main
ones in this project.
```
    if process.check_menu(order) and process.check_resources(order) and money.checking(order):
        process.brewing(order)
        print(f"Here is ${money.change} in change.")
        print(f"Here is your {order}☕, enjoy.")
```

---

_Credits to: 100-Days of Code Course on Udemy._