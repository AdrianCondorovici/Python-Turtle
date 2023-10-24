from turtle import Turtle

class Ball:
    def __init__(self):
        self.ball=Turtle()
        self.ball.penup()
        self.ball.shape("circle")
        self.ball.color("red")