
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guess = []
while len(guess) < 50:
    user_answer = turtle.textinput(
        title=f"{len(guess)}/50 states guessed", prompt="Enter a State").title()

    if user_answer in all_states:
        guess.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == user_answer]
        t.setpos(x=int(state_data.x), y=int(state_data.y))
        t.write(user_answer)
    elif user_answer == "exit" or "Exit":
        missed = []
        for i in all_states:
            if i not in guess:
                missed.append(i)
        new_data = pd.DataFrame(missed)
        new_data.to_csv("missed-states.csv")
        break


screen.exitonclick()
