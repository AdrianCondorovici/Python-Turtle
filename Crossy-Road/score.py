from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(250,250)
        self.write(f"Scor: {self.score}", align= "center", font=("Arial",24,"normal"))
        self.hideturtle()

    def scor(self):
        self.clear()
        self.score+=1
        self.write(f"Scor: {self.score}", align= "center", font=("Arial",24,"normal"))

    def over(self):
        self.clear()
        self.penup()
        self.goto(0,0)
        self.wrizte("Game over", align="center", font=("Arial", 70,"normal"))