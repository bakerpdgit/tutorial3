from math import pi

class Circle:
    """
        Circle has a radius
    """
    def __init__(self, radius: float) -> None:
        self._radius: float = radius

    @property
    def radius(self):
        return self._radius

    def circumference(self):
        return 2 * pi * self._radius

    def area(self):
        return pi * self._radius * self._radius

    # alternate constructor
    @classmethod
    def from_diameter(cls, diameter: float):
        return cls(radius=diameter / 2)

class PrintableCircle(Circle):
    """
        A circle with a string representation method
    """
    def __repr__(self):
        return f"PrintableCircle({self._radius})"

# make a new circle using the alternate constructor
circle: Circle = PrintableCircle.from_diameter(2)
print(circle, circle.circumference(), circle.area())
