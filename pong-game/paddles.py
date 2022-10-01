from os import sep
from turtle import Turtle, turtles

class Paddles(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("coral")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        
    def up(self):
        new_y = self.ycor() + 30
        self.goto(x = self.xcor() ,y = new_y)
    def down(self):
        new_y = self.ycor() - 30
        self.goto(x = self.xcor() , y = new_y)
