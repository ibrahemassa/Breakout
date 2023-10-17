from turtle import Screen
from player import Player
from ball import Ball
from box import Box
from score import Score

screen = Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("Breakout")
screen.listen()
screen.tracer(0)

pad = Player(-280)
screen.onkey(pad.move_right, 'Right')
screen.onkey(pad.move_left, 'Left')

ball = Ball()

main_box = Box(-420, 320)
boxes = [main_box]

score = Score()


is_on = True

for i in range(69):
    if boxes[-1].xcor() < 420:
        box = Box(boxes[-1].xcor()+65, boxes[-1].ycor())
    else:
        box = Box(boxes[0].xcor(), boxes[-1].ycor()-60)
    boxes.append(box)

while is_on:
    screen.update()
    ball.move()

    if ball.ycor() >= 330:
        ball.bounce_y()

    if ball.xcor() >= 430 or ball.xcor() <= -430:
        ball.bounce_x()

    if (
            pad.xcor() - 110 <= ball.xcor() <= pad.xcor() + 110 and
            pad.ycor() - 10 <= ball.ycor() <= pad.ycor() + 10
    ):
        ball.bounce_y()

    for box in boxes:
        if ball.distance(box) <= 30:
            box.hideturtle()
            box.setpos(1000, 1000)
            # ball.bounce_x()
            ball.bounce_y()
            score.add_score()

    if ball.ycor() < -345:
        is_on = False


screen.exitonclick()
