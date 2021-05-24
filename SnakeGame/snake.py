from turtle import Turtle

MOVE_DISTANCE = 20
MOVE_90 = 90

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.speed("fastest")
        new_segment.pu()
        if pos == (0, 0):
            new_segment.color("cornflower blue")
        else:
            new_segment.color("white")
        new_segment.goto(pos)
        self.snake_body.append(new_segment)

    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000,1000)
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def move(self):
        for idx in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[idx - 1].xcor()
            y = self.snake_body[idx - 1].ycor()
            self.snake_body[idx].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def check_wall_collision(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if self.head.xcor() > 285:
            self.head.goto(-285, y)
        elif self.head.xcor() < -285:
            self.head.goto(285, y)
        elif self.head.ycor() > 285:
            self.head.goto(x, -285)
        elif self.head.ycor() < -285:
            self.head.goto(x, 285)

    def check_tail_collision(self):
        for segment in self.snake_body[1:]:
            if self.head.distance(segment) < 10:
                return True


