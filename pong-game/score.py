from turtle import Turtle,Screen

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.x_score = 0
        self.y_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.y_score , align = "center" , font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.x_score , align = "center" , font=("Courier", 80, "normal"))

    def x_update(self):
        
        self.x_score += 1
        self.update_score()
    def y_update(self):
        
        self.y_score += 1
        self.update_score()
        