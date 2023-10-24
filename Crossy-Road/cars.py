from turtle import Turtle
import random
class Cars():
    def __init__(self):
        self.colors = ["red", "blue", "green", "purple", "pink", "orange", "black", "brown"]
        self.cars = []
        self.s=5
        self.speed=1
        for _ in range(10):
            self.traffic()

    def chance (self):
        chance=random.randint(1,6)
        if chance <= self.speed:
            self.traffic()

    def traffic(self):
        x = random.choice(range(400, 600))
        y = random.choice(range(-280, 300))
        color = random.choice(self.colors)
        new_car = Turtle("square")
        new_car.color(color)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.penup()
        new_car.goto(x, y)
        self.cars.append(new_car)
        print(len(self.cars))

    def move(self):
        for drive in self.cars:
            drive.forward(self.s)

    def level_up(self):
        self.s +=5
        self.speed +=1

