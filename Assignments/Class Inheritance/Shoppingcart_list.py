import time
items_list = []
price_list = []
# Create the parent class ShoppingCart
class ShoppingCart():

    def __init__(self, customer_name):
        self.customer_name = customer_name

    # Method that stores product and price in two separate lists
    def add_item(self, product, price):
        items_list.append(product)
        price_list.append(price)
        return f"--{self.customer_name} added {product} to shopping cart."

    def remove_item(self, product, price):
        # Check if the product is in the shopping cart
        if product in items_list and price in price_list:
            # Method that removes product and price from a list
            items_list.remove(product)
            price_list.remove(price)
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
    
    def remove_item(self, product="Apple", price=2):
        return super().remove_item(product, price)

class Banana(ShoppingCart):

    def add_item(self, product="Banana", price=1):
        return super().add_item(product, price)

    def remove_item(self, product="Banana", price=1):
        return super().remove_item(product, price)

class Potato_chips(ShoppingCart):

    def add_item(self, product="Potato Chips", price=4):
        return super().add_item(product, price)

    def remove_item(self, product="Potato Chips", price=4):
        return super().remove_item(product, price)

class Gummy_bears(ShoppingCart):

    def add_item(self, product="Gummy Bears", price=5):
        return super().add_item(product, price)

    def remove_item(self, product="Gummy Bears", price=5):
        return super().remove_item(product, price)

class Chocolate_bar(ShoppingCart):

    def add_item(self, product="Chocolate Bar", price=3):
        return super().add_item(product, price)

    def remove_item(self, product="Chocolate Bar", price=3):
        return super().remove_item(product, price)

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
        if items_list:
            print("----Current shopping cart----")
            for items in items_list:
                print(items)
            print("-----------------------------")
            total = sum(price_list)
            print(f"Total: ${total}.")
            time.sleep(1.5)
            op_choice()

        else:
            print("There are no items in your shopping cart.")
            time.sleep(1)
            op_choice()

    # If "3" is inputted, checkout and finish the script
    elif operator == "4":
        total = sum(price_list)
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

