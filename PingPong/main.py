from turtle import Turtle, Screen
import time

from ball import Ball
from paddle import Paddle
from score import Score

ball = Ball()

screen = Screen()
screen.setup(900, 600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)

first_player = Paddle(-1)
second_player = Paddle(1)

score = Score()


def center_line():
    line = Turtle()
    line.color("white")
    line.speed("fastest")
    line.width(5)
    line.hideturtle()
    line.pu()
    screen.update()
    line.goto(0, 280)
    line.setheading(270)

    for _ in range(19):
        line.pd()
        line.forward(15)
        line.pu()
        line.forward(15)


center_line()

screen.listen()
screen.onkey(key="Up", fun=second_player.move_up)
screen.onkey(key="Down", fun=second_player.move_down)

screen.onkey(key="w", fun=first_player.move_up)
screen.onkey(key="s", fun=first_player.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.speed_val)
    ball.start_moving()

    # Up Down Wall Bounce
    if ball.ball.ycor() > 280 or ball.ball.ycor() < -280:
        ball.bounce_wall()

    elif ball.ball.xcor() > 420:
        ball.reset_ball()
        score.left_paddle_score += 1
    elif ball.ball.xcor() < -420:
        ball.reset_ball()
        score.right_paddle_score += 1

    # Paddle Collision
    elif ball.ball.distance(second_player.paddle) < 60 and ball.ball.xcor() > 350 and ball.ball.xcor() < (second_player.paddle.xcor()):
        ball.bounce_paddle()
        ball.speed_val *= 0.9
    elif ball.ball.distance(first_player.paddle) < 60 and ball.ball.xcor() < -350 and ball.ball.xcor() < (first_player.paddle.xcor()):
        ball.speed_val *= 0.9
        ball.bounce_paddle()

    score.display()

    screen.update()

screen.exitonclick()
# game_is_on = False
#         game_over = Turtle()
#         game_over.color("cornflower blue")
#         game_over.ht()
#         game_over.write("GAME  OVER", False, "center", ("Consolas", 20, "normal"))
