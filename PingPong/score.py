from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        self.score = Turtle()
        self.score.ht()
        self.score.pu()
        self.display()

    def display(self):
        self.score.clear()
        self.score.goto(-100, 175)
        self.score.color("cyan")
        self.score.write(f"{self.left_paddle_score}", False, "center", ("Consolas", 60, "bold"))
        self.score.goto(100, 175)
        self.score.color("orange red")
        self.score.write(f"{self.right_paddle_score}", False, "center", ("Consolas", 60, "bold"))

