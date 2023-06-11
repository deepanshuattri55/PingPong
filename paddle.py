from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,pos) -> None:
        super().__init__()
        self.shape('square')
        self.shapesize(4,1)
        self.color('white')
        self.penup()
        self.goto(pos,0)


    def move_up(self):
        if self.ycor() < 260:
            ycor =  self.ycor() +20
            self.goto(self.xcor(), ycor )
        
    
    def move_down(self):
        if self.ycor() > -260:
            ycor =  self.ycor() -20
            self.goto(self.xcor(), ycor )

    
