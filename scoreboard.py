from turtle import Turtle
from unittest import registerResult


class ScoreBoard(Turtle):
    def __init__(self, BANNER_X, BANNER_Y):
        super().__init__()
        self.score = 0
        self.high_score = 0

        with open("scoreboard.txt") as file:
            contents = int(file.read())
            print(f"high score is: {contents}")

        self.penup()
        self.hideturtle()
        self.color("white")
        self.refresh()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scoreboard.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.clear()
        self.refresh()

    def increase_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.goto(0, 270)
        self.clear()
        self.write(f"Current Score = {self.score}, High Score = {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
