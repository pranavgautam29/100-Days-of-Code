import random
from turtle import Turtle , Screen
import time

from scoreboard import Scoreboard
from snake_class import Snake
from food import Food

screen = Screen()
screen.setup(width = 600,height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False
    #Detect collision with tail
    for i in snake.snakes[1:]:
        if snake.head.distance(i)<10:
            score.game_over()
            game_is_on= False
        
    
    
    
    

        
        

        
        
        
        

screen.exitonclick()