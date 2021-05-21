from turtle import Turtle


class Score:
    def __init__(self):
        self.display_turtle = Turtle()
        self.score_val = 0
        self.display_turtle.color("white")
        self.display_turtle.pu()
        self.display_turtle.hideturtle()
        self.display_turtle.goto(0, 250)
        self.display(self.score_val)

    def display(self, pts):
        self.score_val += pts
        self.display_turtle.clear()
        self.display_turtle.write(f"Score: {self.score_val}", move=False, align="center", font=("Dubai", 20, "normal"))

    def game_over(self):
        self.display_turtle.home()
        self.display_turtle.write("GAME OVER.", False, "center", ("Courier", 20, "normal"))

