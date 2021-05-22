from turtle import Turtle


class ScoreBoard:
    def __init__(self):
        self.display_turtle = Turtle()
        self.display_turtle.ht()
        self.display_turtle.pu()
        self.display_turtle.color("steel blue")
        self.level = 0
        self.display_turtle.goto(-250, 250)
        self.score_update()

    def score_update(self):  # update the level by clearing previous write
        self.display_turtle.clear()
        self.level += 1
        self.display_turtle.write(f"Level {self.level}", False, "center", ("Consolas", 20, "bold"))

    def game_over(self):  # end the game, by printing
        self.display_turtle.goto(0, -260)
        self.display_turtle.write("GAME OVER", False, "center", ("Consolas", 25, "bold"))
