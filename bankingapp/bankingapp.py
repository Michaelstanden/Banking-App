#Imports
from tkinter import *
import os
from PIL import Imagetk, Image

#Main screen
master = Tk()
master.title('Banking App')

#Functions
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()   
    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg="red", text="All fields required *")
        return

    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red", text="Account name already exists please choose another name *")
        else:
            new_file = open(name, "w")
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write(password+'\n')
            new_file.close
            notif.config(fg="green", text="Account Successfully added")


def register():
    #Variables
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    #Register screen
    register_screen = Toplevel(master)
    register_screen.title('Register')
    
    #Lables
    Label(register_screen, text="Please enter your details below to register", font=("Calibri", 12)).grid(row=0, sticky=N, pady=10)
    Label(register_screen, text="Name", font=("Calibri", 12)).grid(row=1, sticky=W, pady=10)
    Label(register_screen, text="Age", font=("Calibri", 12)).grid(row=2, sticky=W, pady=10)
    Label(register_screen, text="Gender", font=("Calibri", 12)).grid(row=3, sticky=W, pady=10)
    Label(register_screen, text="Password", font=("Calibri", 12)).grid(row=4, sticky=W, pady=10)
    notif = Label(register_screen, font=("Calibri", 12))
    notif.grid(row=6, sticky=N, pady=10) 

    #Entries
    Entry(register_screen, text_variable=temp_name).grid(row=1, column=0)
    Entry(register_screen, text_variable=temp_age).grid(row=2, column=0)
    Entry(register_screen, text_variable=temp_gender).grid(row=3, column=0)
    Entry(register_screen, text_variable=temp_password, show="*").grid(row=4, column=0)

    #Button
    Button(register_screen, text="Register", font=('Calibri', 12)).grid(row=5, stickyN)
def login():
    print('This is a log in page')

#Image Import
img = Image.open("currency.jpg")
img = img.resize((150,150))
img = Image.Tk.PhotoImage(img)

#Lables
Label(master, text  "Custom Banking Beta", font=('Calibri',14)).grid(row=0, sticky=N, pady=10)
Label(master, text  "Secure Banking online", font=('Calibri',12)).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2, sticky=N, pady=15)

#Buttons
Button(master, text="Register", font('Calibiri'12), width=20, command=register).grid(row=3, sticky=N)
Button(master, text="Login", font('Calibiri'12), width=20, command=login).grid(row=4, sticky=N, pady=10)
#added so application can stay in a loop and does not crash
master.mainloop()
