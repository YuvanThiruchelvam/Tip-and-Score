print('Ellam Pugazhum iraivanuke')

import turtle
import os

# score
score_1 = 0

wn = turtle.Screen()

wn.title('First_game')
wn.bgcolor('magenta')
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle_1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.color('cyan')
paddle_1.shape('square')

paddle_1.penup()
paddle_1.goto(0, -200)
paddle_1.shapesize(stretch_wid=1, stretch_len=5)

# paddle_2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.color('dark blue')
paddle_2.shape('square')
paddle_2.penup()
paddle_2.goto(0, 250)
paddle_2.shapesize(stretch_wid=1, stretch_len=42)

# ball

ball = turtle.Turtle()
ball.color('black')
ball.speed(0)
ball.shape('circle')
ball.penup()
ball.goto(0, 0)

ball.dx = 4
ball.dy = 4

# pen
pen = turtle.Turtle()
pen.speed()
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(' Score 0 ', align='center', font=(' aerial', 24, ' bold'))


# function
def paddle_1_Right():
    x = paddle_1.xcor()
    x += 60
    paddle_1.setx(x)


def paddle_1_Left():
    x = paddle_1.xcor()
    x -= 60
    paddle_1.setx(x)


# keyboard
wn.listen()
wn.onkeypress(paddle_1_Right, "Right")
wn.onkeypress(paddle_1_Left, "Left")

while True:
    wn.update()

    # ballmove
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # borders

    if ball.xcor() > (380):
        ball.setx(380)
        ball.dx *= -1
        os.system("afplay po&")

    if ball.xcor() < (-380):
        ball.setx(-380)
        ball.dx *= -1

    if ball.ycor() < (-290):
        ball.goto(0, 0)
        ball.dy *= -1

        wn.bgcolor('light green')
        pen.clear()
        pen.goto(0, 0)
        pen.color('red')
        pen.write(' Your score is {}  '.format(score_1), align='center', font=(' aerial', 24, ' bold'))
        pen.goto(0, -100)
        pen.color('red')
        pen.write(' Well Done ', align='center', font=(' aerial', 24, ' bold'))
        ball.goto(100, 100)
        ball.dy = 0

    if ball.ycor() > (290):
        ball.sety(290)
        ball.dy *= -1

    # paddle and ball collisions

    if (ball.ycor() < - 190 and ball.ycor() > -200) and (
            ball.xcor() < paddle_1.xcor() + 60 and ball.xcor() > paddle_1.xcor() - 60):
        ball.sety(-190)
        ball.dy *= -1

    if (ball.ycor() < 250 and ball.ycor() > 240) and (
            ball.xcor() < paddle_2.xcor() + 420 and ball.xcor() > paddle_2.xcor() - 420):
        ball.sety(240)
        ball.dy *= -1
        score_1 += 500
        pen.clear()
        pen.color('yellow')
        pen.write(' Score = {} '.format(score_1), align='center', font=(' aerial', 24, ' bold'))
        if score_1 == 4500:
            ball.dx = 6
            ball.dy = 6

        elif score_1 == 6500:
            ball.dx = 9
            ball.dy = 9

        
