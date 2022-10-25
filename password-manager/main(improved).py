from tkinter import messagebox
from tkinter import *
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_pass():
    
    ltr = random.randint(8,9)
    n = random.randint(2,4)
    sy = random.randint(2,4)


    password = ""
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
        'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
        'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    s = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
        '*', '(', ')', '<']
    pass_letter = [random.choice(l) for n in range(ltr)]
    pass_num = [random.choice(num) for n in range(n)]
    pass_sym = [random.choice(s) for n in range(sy)]
    password_list = pass_letter + pass_num + pass_sym
    
    random.shuffle(password_list)
    password = "".join(password_list)

    pass_input.insert(0,password)

    
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    website = website_input.get()
    username = email_input.get()
    password = pass_input.get()
    new_data = {
        website : {
            "email" : username,
            "password" : password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(
            title="ERROR", message="Please don't leave any field empty.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                
        except FileNotFoundError:
            with open("data.json" , "w") as file:
                json.dump(new_data,file,indent=4)
        else:
            data.update(new_data)
            
            with open("data.json", "w") as file:
                json.dump(data,file,indent=4)
        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            pass_input.delete(0, END)

def find_password():
    website = website_input.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title=website,message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            passw = data[website]["password"]
            messagebox.showinfo(title=website ,message=f"Email:{email}\nPassword:{passw}")
        else:
            messagebox.showerror(title=website,message=f"No record for {website} found")    
        


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")


canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
window.config(padx=50, pady=50)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:")
label1.grid(column=0, row=1)
label1.focus()
label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2)
label3 = Label(text="Password:")
label3.grid(column=0, row=3)

website_input = Entry(width=20)
website_input.grid(column=1, row=1)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "xyz@email.com")

pass_input = Entry(width=22)
pass_input.grid(column=1, row=3)

button1 = Button(text="Generate", width=10,command=random_pass)
button1.grid(column=2, row=3)

button2 = Button(text="Add", width=32, command=add_data)
button2.grid(column=1, row=4, columnspan=2)
button3 = Button(text="Search",width=12,command=find_password)
button3.grid(column=2,row=1)
window.mainloop()
