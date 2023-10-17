from turtle import Turtle
import random as rd

colors = ['LightGreen', 'aquamarine', 'BlueViolet', 'LightPink1', 'chocolate']


class Box(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(2, rd.randint(2, 3))
        self.color(rd.choice(colors))
        self.setpos(x, y)
