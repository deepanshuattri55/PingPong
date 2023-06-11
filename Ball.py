from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x=10
        self.y=10
        self.ballspeed= .1
        # self.shapesize(20,20)


    def move(self):
        x=self.xcor() + self.x
        y= self.ycor() + self.y
        self.goto(x,y)

    def topcollision(self):
        self.y *=-1 
        x=self.xcor() + self.x
        y= self.ycor() + self.y
        self.goto(x,y)

    def bottomcollision(self):
        self.y *=-1 
        x =self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x,y)


    def padcollision(self):
        self.ballspeed *= 0.9
        self.x *=-1 
        x =self.xcor() + self.x 
        y = self.ycor() + self.y 
        self.goto(x,y)


    def reset(self) :
         self.goto(0,0)
         self.ballspeed=0.1
         self.x*=-1
