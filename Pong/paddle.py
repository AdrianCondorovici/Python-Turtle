from turtle import Turtle

class Paddle:
    def __init__(self):
        self.left_paddle=Turtle()
        self.right_paddle=Turtle()
        self.create(self.left_paddle)
        self.left_paddle.goto(-350,0)
        self.create(self.right_paddle)
        self.right_paddle.goto(350,0)
    def create(self,paddle):
        paddle.shape("square")
        paddle.shapesize(stretch_wid=5,stretch_len=1)
        paddle.color("red")
        paddle.penup()

    def left_go_up(self):
        if self.left_paddle.ycor() <  240:
            new_y = self.left_paddle.ycor() + 40
            self.left_paddle.goto(self.left_paddle.xcor(), new_y)

    def left_go_down(self):
        if self.left_paddle.ycor() > - 240:
            new_y = self.left_paddle.ycor() - 40
            self.left_paddle.goto(self.left_paddle.xcor(), new_y)

    def right_go_up(self):
        if self.right_paddle.ycor() <  240:
            new_y = self.right_paddle.ycor() + 40
            self.right_paddle.goto(self.right_paddle.xcor(), new_y)

    def right_go_down(self):
        if self.right_paddle.ycor() > - 240:
            new_y = self.right_paddle.ycor() - 40
            self.right_paddle.goto(self.right_paddle.xcor(), new_y)