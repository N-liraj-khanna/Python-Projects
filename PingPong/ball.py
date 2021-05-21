from turtle import Turtle


class Ball:
    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.color("cornflower blue")
        self.ball.pu()
        self.ball.speed(0)
        self.y_move = 10
        self.x_move = 10
        self.speed_val = 0.1

    def start_moving(self):
        x = self.ball.xcor() + self.x_move
        y = self.ball.ycor() + self.y_move
        self.ball.goto(x, y)

    def bounce_wall(self):
        self.y_move = -self.y_move

    def bounce_paddle(self):
        self.x_move = -self.x_move

    def reset_ball(self):
        self.ball.home()
        self.x_move *= -1
        self.y_move *= -1
        self.speed_val = 0.1


