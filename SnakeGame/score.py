from turtle import Turtle


class Score:
    def __init__(self):
        self.display_turtle = Turtle()
        self.score_val = 0
        self.display_turtle.color("white")
        self.display_turtle.pu()
        self.display_turtle.hideturtle()
        self.display_turtle.goto(0, 250)
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.display(self.score_val)

    def display(self, pts):
        self.score_val += pts
        self.display_turtle.clear()
        self.display_turtle.write(f"Score: {self.score_val}     High Score: {self.high_score}", move=False, align="center", font=("Dubai", 20, "normal"))

    def reset(self):
        with open("high_score.txt", "w") as file:
            file.write(str(max(self.high_score, self.score_val)))
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())
        self.score_val = 0
        self.display(self.score_val)

    # def game_over(self):
    #     self.display_turtle.home()
    #     self.display_turtle.write("GAME OVER.", False, "center", ("Courier", 20, "normal"))

