from math import pi

class Shape:

    def __init__(self):
        pass

    def area(self):
        pass

class Rectangle(______):
    def __init__(self, length, width):
        _____().__init__()
        self.length = length
        self.width = width

    def area(self):
        return _______* _______

class Circle(_____):
    def __init__(self, radius):
        super().________
        self.radius = radius

    def ____(self):
        return pi * _________ ** 2

class Triangle(_____):
    def __init__(self, base, height):
        _____().__init__()
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * ________ * _________

shapes = [Rectangle(4, 5), Circle(3), Triangle(6, 8)]

for shape in _______:
    print("Area of shape:", shape.______())