
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    
    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, height):
        super().__init__(self, height)
        self.height = height

    def area(self):
        return self.length * self.width * self.height

print(str(Square(3, 3)))

