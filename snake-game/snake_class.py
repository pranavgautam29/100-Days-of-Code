from turtle import Turtle, down
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)
            
    def move(self):
        for num in range(len(self.snakes) - 1,0,-1):
            x = self.snakes[num-1].xcor()
            y = self.snakes[num-1].ycor()
            self.snakes[num].goto(x,y)
        self.snakes[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    def add_segment(self,positions):
        new_snake = Turtle()
        new_snake.shape("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(positions)
        self.snakes.append(new_snake)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    



