from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.9)
        self.color('green')
        self.speed('fastest')
        self.refresh()
    def refresh(self):
        randx = random.randint(-270, 250)
        randy = random.randint(-270, 250)
        self.goto(randx, randy)

