import time
from turtle import Screen
from car import Car
from my_turtle import MyTurtle

# screen things
from score import ScoreBoard

screen = Screen()
screen.setup(700, 600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

# user/player turtle
my_turtle = MyTurtle()
# score board
score = ScoreBoard()

# listens to keystrokes
screen.listen()
screen.onkey(my_turtle.move_up, "Up")

# all cars created saved in this list
my_cars = []

# Switch for turning on and off the game
game_in_on = True
speed_val = 0.1  # tracks the speed
iterations = 0  # keep track of iterations
create_car_at_iteration = 7  # create a car of this iteration (using modulo operator)
while game_in_on:
    # creating a new car for every 7th(will change as the game level increases) iteration
    if iterations % create_car_at_iteration == 0:
        car = Car()
        my_cars.append(car)

    time.sleep(speed_val)  # speed

    # Check for level up and increase speed of cars
    if my_turtle.my_turtle.ycor() > 240:
        my_turtle.my_turtle.sety(-250)  # ctakes turtle back to home
        score.score_update()  # increases level
        speed_val *= 0.9  # increases speed by a little quantity (0.1*0.9)
        create_car_at_iteration -= 1  # increases amount of cars created

    for my_car in my_cars:
        # moving each of the cars added in the list for every iteration
        my_car.move()

        # detecting car/user collision
        if my_car.car.distance(my_turtle.my_turtle) < 40:
            score.game_over()
            game_in_on = False
            break

    if my_cars[0].car.xcor() < -400:
        # objects(cars) created will be destroyed once it reaches the end of the wall
        del my_cars[0].car
        # delete cars from list too, just to decrease time complexity
        my_cars.pop(0)

    screen.update()  # update the screen for every iteration (switching off animation)
    iterations += 1  # track of iteration

screen.exitonclick()
