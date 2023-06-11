from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.updateScore()
        
        

    def updateScore(self):
        self.clear()
        self.goto(-270,270)
        self.write(f'Score: {self.lscore}',align='left',font=('Courier',18,))
        self.goto(250,270)
        self.write(f'Score: {self.rscore}',align='right',font=('Courier',18,'normal'))


    def lpoint(self):
        self.lscore += 1
        self.updateScore()

    def rpoint(self):
        self.rscore += 1
        self.updateScore()
        
