import time
from turtle import Screen

from Food import Food
from score import Score
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

food = Food()
snake = Snake()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)


is_on = True
while is_on:
    screen.update()
    time.sleep(0.5)
    snake.move()

    if food.snake_food.distance(snake.head) < 15:
        food.change_pos()
        score.display(1)
        snake.extend()
    elif snake.check_wall_collision() or snake.check_tail_collision():
        score.reset()
        snake.reset()


screen.exitonclick()

