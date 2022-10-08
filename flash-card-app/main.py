from cgitb import text
from locale import currency
from tkinter import *
from numpy import flip
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("french_words.csv")
data_dict = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas1.itemconfig(card_title , text="French",fill="black")
    canvas1.itemconfig(card_word,text= current_card["French"],fill="black")
    canvas1.itemconfig(card_img,image=img1)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas1.itemconfig(card_title,text="English",fill="white")
    canvas1.itemconfig(card_word,text= current_card["English"],fill="white")
    canvas1.itemconfig(card_img,image=img2)

def is_known():
    data_dict.remove(current_card)
    next_card()




#------------------------------- UI Setup----------------------------
window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Flash Card App")

flip_timer = window.after(3000, func=flip_card)

img1 = PhotoImage(file="card_front.png")
img2 = PhotoImage(file="card_back.png")
canvas1 = Canvas(width=800,height=526)
card_img = canvas1.create_image(400,263,image=img1)
card_title = canvas1.create_text(400,150,text="", font=("Ariel",40,"italic"))
card_word = canvas1.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas1.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas1.grid(row=0,column=0,columnspan=2)

wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

check_img = PhotoImage(file="right.png")
check_button = Button(image=check_img,highlightthickness=0,command=is_known)
check_button.grid(row=1,column=1)
next_card()

window.mainloop()

