from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.current = 0
        self.setpos(0, -340)
        self.write(f"{self.current}", align="center", font = ("Arial", 30, "normal"))
        self.ht()

    def add_score(self):
        self.current += 1
        self.clear()
        self.write(f"{self.current}", align="center", font = ("Arial", 30, "normal"))
