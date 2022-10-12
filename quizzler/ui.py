
from tkinter import *

from setuptools import Command
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.label = Label(text=f"Score: {self.score}", highlightthickness=0)
        self.label.config(bg=THEME_COLOR,padx=20,pady=20,fg="white")
        self.label.grid(column=1,row=0)
        self.canvas = Canvas(width=300,height=250)
        self.question_text = self.canvas.create_text(150,125,text="Question??" , font=("Arial" , 20 , "italic"),fill=THEME_COLOR,width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        img1 = PhotoImage(file="true.png")
        img2 = PhotoImage(file="false.png")
        self.button1 = Button(image=img1,highlightthickness=0,command=self.true)
        self.button1.grid(column=0,row=2)
        self.button2 = Button(image=img2,highlightthickness=0,command=self.false)
        self.button2.grid(row=2,column=1)
        

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        

        if self.quiz.still_has_questions():
            
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text , text= q_text)
        else:
            
            self.canvas.itemconfig(self.question_text , text="You have completed the quiz!!")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")
    def true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
            self.label.config(text=f"Score: {self.score}")
            
            
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000,self.get_next_question)




        

