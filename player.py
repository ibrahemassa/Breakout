from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('red')
        self.shapesize(1, 10)
        self.setpos(0, position)
        self.speed = 35

    def move_right(self):
        self.setpos(self.xcor()+self.speed, self.ycor())

    def move_left(self):
        self.setpos(self.xcor()-self.speed, self.ycor())
