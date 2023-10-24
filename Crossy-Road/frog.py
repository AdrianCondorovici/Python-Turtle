from turtle import Turtle

class Frog():
    def __init__(self):
        self.frog = Turtle("turtle")
        self.frog.color("red")
        self.frog.penup()
        self.frog.setheading(90)
        self.frog.goto(0, -280)

    def frog_up(self):
        self.frog.forward(10)
