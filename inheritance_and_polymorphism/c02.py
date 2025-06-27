from math import pi


class Rectangle:
    """
        Class for a rectangle
        A rectangle is minimally defined using its length and width
    """
    def __init__(self, length: float, width: float) -> None:
        self.__length = length
        self.__width = width

    '''GETTERS'''

    @property
    def length(self) -> float:
        return ____________

    @property
    def width(self) -> float:
        return ___________

    '''AREA AND PERIMETER'''

    def area(self) -> float: # a polymorphic method
        return self.__length * _______

    def perimeter(self) -> float: # a polymorphic method
        return 2 * (________ + ________)

    '''SPECIAL METHODS'''

    # string representation method
    def __repr__(self) -> str:
        return f"Rectangle(length={self.__length}, width={self.__width})"

    # equality operator method
    # we must first check if the object is a rectangle, then we check if their attributes are the same in any order
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Rectangle) and  \
                sorted([________, _______]) == sorted([_______, ________])


class Circle:
    """
        Class for a circle
        A circle is minimally defined using its radius
    """
    def __init__(self, radius: float) -> None:
        self.__radius = _______

    '''GETTERS'''

    @property
    def radius(self) -> float:
        return _______

    '''AREA AND PERIMETER'''

    def area(self) -> float: # a polymorphic method
        return pi * _______ * _______

    def perimeter(self) -> float: # a polymorphic method
        return 2 * ______ * ________

    '''SPECIAL METHODS'''

    # string representation method
    def ___________(self) -> str:
        return f"Circle(radius={self.__radius}"

    # equality operator method
    def ___________(self, other: object) -> bool:
        return isinstance(other, Circle) and ___________ == __________


# using polymorphism to get the area and perimeter of each shape
shapes : list[Rectangle | Circle] = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(shape, shape.area(), shape.perimeter())

# tests for the equality operator
print(Rectangle(3, 4) == Rectangle(3, 4))
print(Rectangle(3, 4) == Rectangle(4, 3))
print(Rectangle(3, 4) == Rectangle(3, 5))
print(Circle(3) == Rectangle(3, 4))
print(Circle(4) == Circle(4))
print(Circle(3) == Circle(5))
