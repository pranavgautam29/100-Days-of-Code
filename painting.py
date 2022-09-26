import random
import turtle as t
t.colormode(255)
rgb = [(239, 234, 226), (220, 158, 84), (39, 109, 150), (120, 163, 191), (150, 63, 87), (217, 232, 222), (203, 134, 157), (180, 160, 34), (32, 131, 95), (122, 179, 152)]

tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.seth(225)
tim.fd(300)
tim.seth(0)
tim.pendown()
num_of_dots = 100
tim.speed("fastest")

for dots in range(1,num_of_dots+1):
     
    tim.dot(20,random.choice(rgb))
    tim.penup()
    tim.fd(50)
    tim.pendown()
    if dots % 10 == 0:
        tim.penup()
        tim.seth(90)
        tim.fd(50)
        tim.seth(180)
        tim.fd(500)
        tim.seth(0)
        tim.pendown()

screen = t.Screen()
screen.exitonclick()
