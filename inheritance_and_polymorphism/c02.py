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
        return self.__length

    @property
    def width(self) -> float:
        return self.__width

    '''AREA AND PERIMETER'''

    def area(self) -> float:
        return self.__length * self.__width

    def perimeter(self) -> float:
        return 2 * (self.__length + self.__width)

    '''SPECIAL METHODS'''

    # string representation method
    def __repr__(self) -> str:
        return f"Rectangle(length={self.__length}, width={self.__width})"

    # equality operator method
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Rectangle) and  \
                sorted([self.__length, self.__width]) == sorted([other.length, other.width])


class Circle:
    """
        Class for a circle
        A circle is minimally defined using its radius
    """
    def __init__(self, radius: float) -> None:
        self.__radius = radius

    '''GETTERS'''

    @property
    def radius(self) -> float:
        return self.__radius

    '''AREA AND PERIMETER'''

    def area(self) -> float:
        return pi * self.__radius * self.__radius

    def perimeter(self) -> float:
        return 2 * pi * self.__radius

    '''SPECIAL METHODS'''

    # string representation method
    def __repr__(self) -> str:
        return f"Circle(radius={self.__radius}"

    # equality operator method
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Circle) and self.__radius == other.radius


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
