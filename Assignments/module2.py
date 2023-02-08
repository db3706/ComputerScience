
# Class defining dimensions and area
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    # Rather than create two separate classes for square and cube, I can
    # define the area formula here to optimize and keep the code short.
    def area(self):
        area = self.length * self.width
        return area

# Class defining cube formula
class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def vol(self):
        # use the super() function to inherit the properties of area() from class Rectangle
        volume = super().area() * self.height
        return volume

# Print
squared = Rectangle(4, 4)
cubed = Cube(4, 4, 4)
print("Squared =",squared.area())
print("Cubed =",cubed.vol())