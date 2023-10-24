from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
import random
x = random.choice([-10, 10])
y = random.choice([-10, 10])
z=0.1
game_is_on = True
screen=Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.title("Pong")
screen.listen()

score= Score()
paddle=Paddle()
screen.onkey(paddle.left_go_up,"w")
screen.onkey(paddle.left_go_down,"s")
screen.onkey(paddle.right_go_up,"Up")
screen.onkey(paddle.right_go_down,"Down")

ball = Ball()

def move(x,y,z):
    if ball.ball.ycor() == 280 or ball.ball.ycor() == -280:
        y = -y
    if abs(ball.ball.ycor() - paddle.left_paddle.ycor()) < 60 and ball.ball.xcor() < -340:
        x = -x
        if z > 0.01:
            z -= 0.015
    if abs(ball.ball.ycor() - paddle.right_paddle.ycor()) < 60 and ball.ball.xcor() > 340:
        x = -x
        if z > 0.01:
            z -= 0.015
    ball.ball.goto(ball.ball.xcor() + x, ball.ball.ycor() + y)
    if ball.ball.xcor() > 380:
        score.scor1()
        x = random.choice([-10, 10])
        y = random.choice([-10, 10])
        z= 0.1
        ball.ball.goto(0,0)
    if ball.ball.xcor() < -380:
        score.scor2()
        x = random.choice([-10, 10])
        y = random.choice([-10, 10])
        z= 0.1
        ball.ball.goto(0,0)
    return(x,y,z)

while game_is_on:
    screen.update()
    time.sleep(z)
    (x,y,z)=move(x,y,z)





screen.exitonclick()

