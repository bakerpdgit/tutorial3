import turtle


class Rectangle:

    COLOURS: dict[str, str] = {
        "red": "#fe0000",
        "green": "#00fe00",
        "blue": "#0000fe"
    }

    def __init__(self, x1: int, y1: int, x2: int, y2: int, colour_name: str):
        self.x1: int = x1
        self.y1: int = y1
        ___.length: int = x2 - x1
        ____ = ___
        ____ = Rectangle.COLOURS[___]

        ___

    def draw(self):
        turtle.penup()
        turtle.pencolor(self.colour)
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        turtle.seth(0)
        turtle.forward(self.length)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(___)
        turtle.right(90)
        turtle.forward(___)
        turtle.done()


rectangle1: Rectangle = Rectangle(-30, 30, 100, 100, "green")
rectangle2: Rectangle = Rectangle(60, -10, 20, 20, "red")
