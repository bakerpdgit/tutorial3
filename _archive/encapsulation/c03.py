class Rectangle:
  def __init__(self, width, height, corner):
    self.__width = width
    self.__height = height
    self.__should_print = True
    self.__corner = corner

  def print(self):
    print("\n" * 10)
    if self.__width == 0:
      ends = ""
      legs = ""
    elif self.__width == 1:
      ends = "+"
      legs = "|"
    else:
      ends = self.__corner + "-" * (self.__width - 2) + self.__corner
      legs = "|" + " " * (self.__width - 2) + "|"
    if self.__height > 0:
      print(ends)
    if self.__height > 1:
      for _ in range(self.__height - 2):
        print(legs)
      print(ends)

  def get_height(self):
    return self.__height

  # Setter method allows additional behaviour to be added
  def set_height(self, height):
    self.__height = height
    if self.__should_print:
      self.print()

  def get_width(self):
    return self.__width

  def set_width(self, width):
    self.__width = width
    if self.__should_print:
      self.print()

  # This getter/setter pair doesn't have anything special going on, but we still use getter and setter methods over
  # public attributes for the sake of encapsulation
  def set_should_print(self, should_print):
    self.__should_print = should_print

  # Different naming convention for boolean getters
  def should_print(self):
    return self.__should_print

  # Getter method allows us to track area by a means other than a dedicated
  # attribute
  def get_area(self):
    return self.__width * self.__height

  # Getter method with no setter for a read-only attribute
  def get_corner(self):
    return self.__corner


rectangle = Rectangle(3, 3, "+")
rectangle.set_width(5)
rectangle.set_should_print(False)
rectangle.set_height(int(input("Enter a new height: ")))
rectangle.set_width(int(input("Enter a new width: ")))
rectangle.set_should_print(True)
rectangle.print()
