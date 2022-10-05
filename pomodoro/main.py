
from ctypes.wintypes import SHORT
from itertools import count
from math import floor
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canva.itemconfig(timer_text,text="00:00")
    label1.config(text="TIMER",fg=GREEN)
    global reps
    reps = 0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN *60)
        label1.config(text="BREAK", fg=PINK)
    elif reps %2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        label1.config(text="BREAK", fg=PINK)
    else:
        count_down(WORK_MIN*60)
        label1.config(text="WORK", fg=RED)
        

    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canva.itemconfig(timer_text,text= f"{count_min}:{count_sec}" )
    if count > 0:
        global timer
        timer = window.after(1000, count_down , count-1)
    else:
        start()
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100,bg = YELLOW)
canva = Canvas(width=200, height=224,bg = YELLOW,highlightthickness=0)
img = PhotoImage(file="tomato.png")
canva.create_image(100,112,image=img) 
timer_text = canva.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME , 35 , "bold"))

canva.grid(column=1,row=1)

label1 = Label(text="Timer", font=(FONT_NAME , 30 ,"normal") , fg=GREEN,bg=YELLOW,highlightthickness=0)
label1.grid(column=1,row=0)
label2 = Label( font=(FONT_NAME , 10 ,"normal") , fg=GREEN,bg=YELLOW,highlightthickness=0)
label2.grid(column=1,row=3)

start_button = Button(text="START",command=start)
start_button.grid(column=0,row=3)

reset_button = Button(text="RESET",command=reset)
reset_button.grid(column=3,row=3)


window.mainloop()
