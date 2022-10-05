from tkinter import *
from turtle import heading

window = Tk()
window.title("Miles to kilometer converter")
window.minsize(width=200 , height=100)


miles_input = Entry(width=10)
miles_input.grid(column=3,row=0)

my_label = Label(text="Miles")
my_label.grid(column=4,row=0)

label2 = Label(text="is equal to")
label2.grid(column=0,row=1)

km_value = Label(text="0")
km_value.grid(column=3,row=1)

km_label = Label(text="km")
km_label.grid(column=4,row=1)

def miles_to_km():
    miles =int(miles_input.get())
    km_result = miles * 1.609
    
    km_value.config(text=km_result)

calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=3,row=2)










window.mainloop()