import time
items_in_cart = {}
# Create the parent class ShoppingCart
class ShoppingCart():

    def __init__(self, customer_name):
        self.customer_name = customer_name

    # Method that stores product and price in a dictionary
    def add_item(self, product, price):
        items_in_cart[product] = price
        return f"--{self.customer_name} added {product} to shopping cart."

    def remove_item(self, product):
        # Check if the product is in the shopping cart
        if product in items_in_cart:
            # Method that removes product and price from a dictionary
            items_in_cart.pop(product)
            return f"--{self.customer_name} removed {product} from shopping cart."
        # If product is not in shopping cart, print the following statement then restart
        else:
            print("Item is not in the shopping cart")
            op_choice()


# Define the child class apple
class Apple(ShoppingCart):
    # define the product as Apple with a price of $2
    def add_item(self, product="Apple", price=2):
        # call the function add_item() from the parent class
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

# Ask the customer for their name
user_name = input("Enter your name: ")
# Print the welcoming statement for the customer
print(f"Hello {user_name}, welcome to the BumaMart digital store.")

# Defines the shopping menu so it can easily be called for frequent use
def shopping_menu():
    print("----Shopping Selection----")
    item_list = ['1. Apple','2. Banana','3. Potato Chips','4. Gummy Bears',"5. Chocolate Bar"]
    for number in item_list:
        print(number)
    print("--------------------------")
 
# Create objects of the child classes
apple = Apple(user_name)
banana = Banana(user_name)
potato_chips = Potato_chips(user_name)
gummy_bears = Gummy_bears(user_name)
chocolate_bar = Chocolate_bar(user_name)


# Function that contains the user's operator choice
def op_choice():

    # Print the operator list
    operator_list = ['1. Add item','2. Remove item','3. View shopping cart','4. Checkout']
    for number in operator_list:
        print(number)
    operator = input("Type a number corresponding to an operator from the list: ")

    # If "1" is inputted, print the shopping menu proceed with adding an item
    if operator == "1":
        shopping_menu()
        add_choice = input("What would you like to add? (Type an integer from the list directly above): ")

        # For example, if 1 is inputted after the prompt, add the item to the shopping cart
        if add_choice == "1":
            print(apple.add_item())
            # Wait 1 second to avoid printing everything all at once
            time.sleep(1)
            op_choice()
        elif add_choice == "2":
            print(banana.add_item())
            time.sleep(1)
            op_choice()
        elif add_choice == "3":
            print(potato_chips.add_item())
            time.sleep(1)
            op_choice()
        elif add_choice == "4":
            print(gummy_bears.add_item())
            time.sleep(1)
            op_choice()
        elif add_choice == "5":
            print(chocolate_bar.add_item())
            time.sleep(1)
            op_choice()
    # If "2" is inputted, proceed with removing a pre-existing item from the shopping cart
    elif operator == "2":
        shopping_menu()
        remove_choice = input("What would you like to remove?: ")

        if remove_choice == "1":
            print(apple.remove_item())
            time.sleep(1)
            op_choice()
        elif remove_choice == "2":
            print(banana.remove_item())
            time.sleep(1)
            op_choice()
        elif remove_choice == "3":
            print(potato_chips.remove_item())
            time.sleep(1)
            op_choice()
        elif remove_choice == "4":
            print(gummy_bears.remove_item())
            time.sleep(1)
            op_choice()
        elif remove_choice == "5":
            print(chocolate_bar.remove_item())
            time.sleep(1)
            op_choice()

    # If "3" is inputted, print the current shopping cart with the total amount
    elif operator == "3":
        if len(items_in_cart) > 0:
            print("----Current shopping cart----")
            for keys in items_in_cart.keys():
                print(keys)
            print("-----------------------------")
            total = sum(items_in_cart.values())
            print(f"Total: ${total}.")
            time.sleep(1.5)
            op_choice()

        else:
            print("There are no items in your shopping cart.")
            time.sleep(1)
            op_choice()

    # If "3" is inputted, checkout and finish the script
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

# https://www.w3schools.com/python/python_dictionaries_add.asp
# https://www.scaler.com/topics/remove-key-from-dictionary-python/
