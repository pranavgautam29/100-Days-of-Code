import random
import turtle
screen = turtle.Screen()
screen.setup(width = 500,height = 400)
choice = screen.textinput(title = "Make your bet", prompt = "Which turtle will win this race? Enter a colour") 
is_race_on = False
if choice:
    is_race_on = True
all_turtles = []

colors = ['purple','blue','green','yellow','orange','red']
y_positions = [0,30,60,90,-30,-60]

for i in range(0,6):
    new_turtle = turtle.Turtle(shape = 'turtle')    
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x= -240,y = y_positions[i])
    all_turtles.append(new_turtle)

while is_race_on:
    
    for tur in all_turtles:
        if tur.xcor() > 230:
            is_race_on = False
            win = tur.pencolor()
            if win == choice:
                print(f"you won")
            else:
                print(win,'won')
        dis = random.randint(0,10)
        tur.forward(dis)
screen.exitonclick()

