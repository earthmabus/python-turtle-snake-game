from turtle import Turtle
import random

SCREEN_X_LEFT = -280
SCREEN_X_RIGHT = 280
SCREEN_Y_TOP = 280
SCREEN_Y_BOTTOM = -280

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(SCREEN_X_LEFT, SCREEN_X_RIGHT)
        random_y = random.randint(SCREEN_Y_BOTTOM, SCREEN_Y_TOP)
        self.goto(random_x, random_y)