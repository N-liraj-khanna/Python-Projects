import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.snake_food = Turtle("circle")
        self.snake_food.speed(0)
        self.snake_food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.snake_food.color("cornflower blue")
        self.snake_food.pu()
        self.change_pos()

    def change_pos(self):
        self.snake_food.goto(random.randint(-250, 250), random.randint(-250, 250))
