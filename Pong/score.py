from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.penup()
        self.goto(250,250)
        self.write(f"{self.score1}", align= "center", font=("Arial",24,"normal"))
        self.hideturtle()
        self.score2 = 0
        self.penup()
        self.goto(-250,250)
        self.write(f"{self.score2}", align= "center", font=("Arial",24,"normal"))
        self.hideturtle()

    def scor1(self):
        self.clear()
        self.score1+=1
        self.write(f"{self.score1}", align= "center", font=("Arial",24,"normal"))
        self.goto(250,250)
        self.write(f"{self.score2}", align= "center", font=("Arial",24,"normal"))
        self.goto(-250,250)

    def scor2(self):
        self.clear()
        self.score2 += 1
        self.write(f"{self.score1}", align= "center", font=("Arial",24,"normal"))
        self.goto(250,250)
        self.write(f"{self.score2}", align= "center", font=("Arial",24,"normal"))
        self.goto(-250,250)