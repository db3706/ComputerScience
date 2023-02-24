items_in_cart = {}

class ShoppingCart():

    def __init__(self, customer_name):
        self.customer_name = customer_name

    # https://www.w3schools.com/python/python_dictionaries_add.asp
    def add_item(self, product, price):
        items_in_cart[product] = price
        print(f"{product} added to shopping cart")

    def remove_item(self, product, price):
        print("Placeholder")

# https://www.scaler.com/topics/remove-key-from-dictionary-python/


class Apple(ShoppingCart):
    def add_item(self, product="apple", price=22):
        return super().add_item(product, price)




items_in_cart["apple"] = 40

apple = Apple("Bro harris")
print(apple)