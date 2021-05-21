from turtle import Turtle, Screen

screen = Screen()


class Paddle:
    def __init__(self, side):
        self.paddle = Turtle("square")
        self.paddle.pu()
        self.paddle.shapesize(stretch_len=1, stretch_wid=5)
        if side == -1:
            self.paddle.color("orange red")
        elif side == 1:
            self.paddle.color("cyan")
        self.paddle.goto(side * 380, 0)

    def move_up(self):
        y = self.paddle.ycor() + 20
        if y < 260:
            self.paddle.sety(y)

    def move_down(self):
        y = self.paddle.ycor() - 20
        if y > -260:
            self.paddle.sety(y)
