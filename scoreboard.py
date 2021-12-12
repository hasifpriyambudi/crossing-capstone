from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

    def score(self):
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", font=FONT)

    def increaseScore(self):
        self.level += 1
        self.clear()
        self.score()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
