import turtle
from turtle import Turtle, Screen
import random
import colorgram

baby = Turtle()
turtle.colormode(255)
baby.speed(0)
baby.hideturtle()
baby.pu()

color_list = [(240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

baby.setheading(220)
baby.forward(350)
baby.setheading(0)

num_of_dots = 100
for dots in range(1, num_of_dots+1):
    baby.dot(20, random.choice(color_list))
    baby.forward(50)
    if dots % 10 == 0:
        baby.setheading(90)
        baby.forward(50)
        baby.setheading(180)
        baby.forward(500)
        baby.setheading(0)

# baby.goto(-300, -250)
#
# for _ in range(9):
#     baby.setpos(-300, baby.ycor()+50)
#     for __ in range(9):
#         baby.forward(50)
#         baby.dot(15, random.choice(color_list))
#

my_screen = Screen()
my_screen.exitonclick()

# Colorgram
# colors = colorgram.extract('image.jpg', 30)
# rgb_colours = []
# for color in colors:
#     rgb_colours.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(rgb_colours)


# Random Colour
# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     rgb = (r, g, b)
#     return rgb
#




# To Draw shapes
# def draw_shape(num_of_sides):
#     for draw in range(1, num_of_sides + 1):
#         baby.forward(100)
#         baby.right(360 / num_of_sides)
#
#
# for sides in range(3, 10):
#     change_color()
#     draw_shape(sides)


# Random Walk
# def random_degree():
#     degrees = [0, 90, 180, 270]
#     return random.choice(degrees)
#
#
# def random_walk():
#     for _ in range(250):
#         baby.color(random_colour())
#         baby.forward(30)
#         baby.setheading(random_degree())
#
#
# baby.pensize(15)
# baby.speed(0)
# random_walk()


# SpiroGraph
# def draw_spirograph(gaps):
#     head = 0
#     while head != 360:
#         baby.pencolor(random_colour())
#         head += gaps
#         baby.circle(100)
#         baby.setheading(head)
#
#
# draw_spirograph(5)
