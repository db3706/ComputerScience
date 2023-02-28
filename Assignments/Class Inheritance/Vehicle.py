
# base vehicle
class Vehicle():
    def __init__(self, colour):
        self.colour = colour

    def description(self):
        print(f"I'm a {self.colour} vehicle!")

# subclass Car definition
class car(Vehicle):
    def __init__(self, colour, style):
        super().__init__(colour)
        self.style = style

    def description(self):
        print(f"I'm a {self.colour} {self.style} car!")

class bus(Vehicle):
    def __init__(self, colour, passenger):
        super().__init__(colour)
        self.passenger = passenger

    def description(self):
        print(f"I'm a {self.colour} bus that can seat {self.passenger} passengers")

class truck(Vehicle):
    def description(self):
        print(f"I'm a {self.colour} truck!")

class bike(Vehicle):
    def description(self):
        print(f"I'm a {self.colour} bike!")

V = Vehicle("Red")
C = car("Black","SUV")
B = bike("White")
T = truck("Blue")
Bu = bus("Yellow","40")

V.description()
C.description()
B.description()
T.description()
Bu.description()