from turtle import Screen
from frog import Frog
from cars import Cars
from score import Score
import time
screen = Screen()
screen.tracer(0)
frog=Frog()
game_is_on = True
screen.setup(width=800, height=600)

screen.listen()
screen.onkey(frog.frog_up, "Up")
cars = Cars()
score = Score()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.chance()
    cars.move()
    for car in cars.cars:
        if frog.frog.distance(car) < 20:
            game_is_on = False
            score.over()
    if frog.frog.ycor() == 300:
        cars.level_up()
        frog.frog.goto(0,-300)
        score.scor()


screen.exitonclick()