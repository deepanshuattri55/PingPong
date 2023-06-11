from turtle import Turtle, Screen
from paddle import Paddle
from Ball import Ball
from score import Score
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.tracer(0)





ball=Ball()
score=Score()

rpad = Paddle(280)
lpad = Paddle(-280)
# lpad = Paddle().createPaddle(-280,0)




screen.listen()
screen.onkey(rpad.move_up , 'Up')
screen.onkey(rpad.move_down , 'Down')
screen.onkey(lpad.move_up , 'w')
screen.onkey(lpad.move_down , 's')
# screen.update()
 

game_is_on =True
while game_is_on:
    time.sleep(ball.ballspeed)
    screen.update()
    #top collision
    
    if ball.ycor() >= 280:
        ball.topcollision()
    
    elif ball.ycor() <= -280:
        ball.bottomcollision()

    elif ball.distance(rpad) < 30:
        ball.padcollision()

    elif ball.distance(lpad) < 30:
        ball.padcollision()

    elif (ball.xcor() >= 300):
        print('point to lpad')
        score.lpoint()
        ball.reset()
        

    elif (ball.xcor() <= -300):
        print('point to rpad')
        score.rpoint()
        ball.reset()
    
    else:
        ball.move()









screen.exitonclick()
