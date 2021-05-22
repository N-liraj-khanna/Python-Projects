import turtle
import random
from turtle import Turtle
from my_turtle import MyTurtle

turtle.colormode(255)


class Car:
    def __init__(self):
        self.car = Turtle("square")
        self.car.shapesize(stretch_len=3, stretch_wid=1.5)
        self.color_generator()
        self.car.pu()
        self.move_to()

    def color_generator(self):  # generates random colour
        self.car.color('#%02X%02X%02X' % (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))

    def move_to(self):  # start a car from random position
        self.car.goto(370, random.randint(-200, 230))

    def move(self):  # start moving the cars by 10 paces
        x = self.car.xcor() - 10
        self.car.setx(x)
