from turtle import Turtle


class MyTurtle:
    def __init__(self):
        self.my_turtle = Turtle("turtle")
        self.my_turtle.color("steel blue")
        self.my_turtle.pu()
        self.my_turtle.setheading(90)
        self.my_turtle.goto(0, -250)
        self.my_turtle.shapesize(stretch_len=1.3, stretch_wid=1.3)

    def move_up(self):  # move the key by 10 paces on keystroke
        y = self.my_turtle.ycor() + 10
        self.my_turtle.sety(y)

