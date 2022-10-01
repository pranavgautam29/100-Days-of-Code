from turtle import Turtle , Screen
from ball import Ball
from score import Score
from paddles import Paddles
import time 

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.title("PONG")

my_screen.setup(width = 800 , height = 600)
my_screen.tracer(0)
ball = Ball()
paddle1 = Paddles((375,0))
paddle2 = Paddles((-375 , 0))
scoreboard = Score()

game_on = True
while game_on:
    my_screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    my_screen.listen()
    my_screen.onkey(paddle1.up,"Up")
    my_screen.onkey(paddle1.down,"Down")
    my_screen.onkey(paddle2.up,"w")
    my_screen.onkey(paddle2.down,"s")
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    #detect collision with paddles
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    if ball.xcor() > 380 :
        ball.reset()
        ball.x_bounce()
        scoreboard.y_update()
        
    if ball.xcor() < -380:
        ball.reset()
        ball.x_bounce()
        scoreboard.x_update() 














my_screen.exitonclick()




