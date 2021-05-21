from turtle import Turtle, Screen

baby = Turtle()
# baby.speed(0)
screen = Screen()


def move_forwards():
    baby.forward(10)


def move_backwards():
    baby.backward(10)


def clock_wise():
    baby.right(10)


def anti_clock_wise():
    baby.left(10)


def clear_all():
    baby.clear()
    baby.pu()
    baby.home()
    baby.pd()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="a", fun=anti_clock_wise)
screen.onkey(key="c", fun=clear_all)

screen.exitonclick()
