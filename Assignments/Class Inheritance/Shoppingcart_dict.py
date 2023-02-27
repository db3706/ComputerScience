import time
items_in_cart = {}
class ShoppingCart():

    def __init__(self, customer_name):
        self.customer_name = customer_name

    # https://www.w3schools.com/python/python_dictionaries_add.asp
    def add_item(self, product, price):
        items_in_cart[product] = price
        return f"--{self.customer_name} added {product} to shopping cart."

    def remove_item(self, product):
        if product in items_in_cart:
            items_in_cart.pop(product)
            return f"--{self.customer_name} removed {product} from shopping cart."
        else:
            print("Item is not in the shopping cart")
            op_choice()
# https://www.scaler.com/topics/remove-key-from-dictionary-python/


class Apple(ShoppingCart):

    def add_item(self, product="Apple", price=2):
        return super().add_item(product, price)

    def remove_item(self, product="Apple"):
        return super().remove_item(product)

class Banana(ShoppingCart):

    def add_item(self, product="Banana", price=1):
        return super().add_item(product, price)

    def remove_item(self, product="Banana"):
        return super().remove_item(product)

class Potato_chips(ShoppingCart):

    def add_item(self, product="Potato Chips", price=4):
        return super().add_item(product, price)

    def remove_item(self, product="Potato Chips"):
        return super().remove_item(product)

class Gummy_bears(ShoppingCart):

    def add_item(self, product="Gummy Bears", price=5):
        return super().add_item(product, price)

    def remove_item(self, product="Gummy Bears"):
        return super().remove_item(product)

class Chocolate_bar(ShoppingCart):

    def add_item(self, product="Chocolate Bar", price=3):
        return super().add_item(product, price)

    def remove_item(self, product="Chocolate Bar"):
        return super().remove_item(product)

user_name = input("Enter your name: ")
print(f"Hello {user_name}, welcome to the BumaMart digital store.")
def shopping_menu():
    print("----Shopping Selection----")
    item_list = ['1. Apple','2. Banana','3. Potato Chips','4. Gummy Bears',"5. Chocolate Bar"]
    for number in item_list:
        print(number)
    print("--------------------------")
 
apple = Apple(user_name)
banana = Banana(user_name)
potato_chips = Potato_chips(user_name)
gummy_bears = Gummy_bears(user_name)
chocolate_bar = Chocolate_bar(user_name)


# Function that contains the user's operator choice
def op_choice():
    operator_list = ['1. Add item','2. Remove item','3. View shopping cart','4. Checkout']
    for number in operator_list:
        print(number)
    operator = input("Type a number corresponding to an operator from the list: ")

    if operator == "1":
        shopping_menu()
        add_choice = input("What would you like to add? (Type an integer from the list directly above): ")

        if add_choice == "1":
            print(apple.add_item())
            op_choice()
        elif add_choice == "2":
            print(banana.add_item())
            op_choice()
        elif add_choice == "3":
            print(potato_chips.add_item())
            op_choice()
        elif add_choice == "4":
            print(gummy_bears.add_item())
            op_choice()
        elif add_choice == "5":
            print(chocolate_bar.add_item())
            op_choice()
    elif operator == "2":
        shopping_menu()
        remove_choice = input("What would you like to remove?: ")

        if remove_choice == "1":
            print(apple.remove_item())
            op_choice()
        elif remove_choice == "2":
            print(banana.remove_item())
            op_choice()
        elif remove_choice == "3":
            print(potato_chips.remove_item())
            op_choice()
        elif remove_choice == "4":
            print(gummy_bears.remove_item())
            op_choice()
        elif remove_choice == "5":
            print(chocolate_bar.remove_item())
            op_choice()
    elif operator == "3":
        print("----Current shopping cart----")
        for keys in items_in_cart.keys():
            print(keys)
        print("-----------------------------")
        op_choice()
    elif operator == "4":
        total = sum(items_in_cart.values())
        print(f"Your total amounts to ${total}.")
        time.sleep(2)
        print("Paying...")
        time.sleep(1)
        print("Processing...")
        time.sleep(2)
        print("Approved!")
        time.sleep(1)
        print(f"Thanks for shopping at BumaMart, {user_name}. Have a nice day!")

# Starts the script
op_choice()