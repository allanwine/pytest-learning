import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        return self.radius == other.radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * 3.14 * self.radius, 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __eq__(self, other):
        if not isinstance(other, Square):
            return False
        return self.side == other.side

    def area(self):
        return round(self.side * self.side, 2)

    def perimeter(self):
        return round(4 * self.side, 2)

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.length == other.length and self.breadth == other.breadth

    def area(self):
        return round(self.length * self.breadth, 2)

    def perimeter(self):
        return round(2 * (self.length + self.breadth), 2)