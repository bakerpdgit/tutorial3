from math import pi
from abc import ABC


# An abstract base class
class Shape(ABC):

    def __init__(self) -> None:
        pass

    def area(self) -> float:
        # NOTE: This is a placeholder (abstract) method that will be overridden by subclasses
        # This makes Shape an abstract class because it has an abstract method and so should not be used directly
        return 0


class Rectangle(______):
    def __init__(self, length: int, width: int) -> None:
        _____().__init__()
        self.length: int = length
        self.width: int = width

    def area(self) -> float:
        return _______ * _______


class Circle(_____):
    def __init__(self, radius: int) -> None:
        super().________
        self.radius: int = radius

    def ____(self) -> float:
        return pi * _________ ** 2


class Triangle(_____):
    def __init__(self, base: int, height: int) -> None:
        _____().__init__()
        self.base: int = base
        self.height: int = height

    def area(self) -> float:
        return 0.5 * ________ * _________


shapes: list[Shape] = [Rectangle(4, 5), Circle(3), Triangle(6, 8)]

for shape in _______:
    print("Area of shape:", shape.______())
