import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)

colors = ["red", "yellow", "purple", "blue", "green", "orange"]
my_color = turtle.textinput("Make you bet!", "Which colour do you choose? ")
y_cor = [-130, -80, -30, 20, 80, 130]

turtle_li = []
for n in range(6):
    turtle_name = Turtle("turtle")
    turtle_name.pu()
    turtle_name.color(colors[n])
    turtle_name.goto(-230, y_cor[n])
    turtle_li.append(turtle_name)

is_on = True
while is_on:
    for turtle in turtle_li:
        if turtle.xcor() > 230:
            if my_color == turtle.fillcolor():
                print(f"Yay! You won, Your {turtle.fillcolor()} turtle is the winner!")
            else:
                print(f"Um! You lose. {turtle.fillcolor()} turtle has won the game")
            is_on = False
            break
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
