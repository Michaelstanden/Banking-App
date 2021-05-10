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
            new_file.write('0')
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


def login_session():
    global login_name
    all_account = os.listdir()
    login_name = temp_log_name.get()
    login_password = temp_login_password.get()
   
    for name in all_account:
        if name == login_name:
            file = open(name, "r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]
            #Account Dashborad
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title("Dashboard")
                #Labels
                Label(account_dashboard, text="Account Dashboard", font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
                Label(account_dashboard, text="Welcome "+name, font=('Calibri', 12)).grid(row=1, sticky=N, pady=5)
                #Buttons
                Button(account_dashboard, text="Personal Details", font=('Calibri', 12), width=30, command=personal_details).grid(row=2, sticky=N, padx=10)
                Button(account_dashboard, text="Deposit", font=('Calibri', 12), width=30, command=deposit).grid(row=3, sticky=N, padx=10)
                Button(account_dashboard, text="Withdraw", font=('Calibri', 12), width=30, command=withdraw).grid(row=4, sticky=N, padx=10)
                Label(account_dashboard).grid(row=5, sticky=N, pady=10)
                return
            else: 
                login_notif.config(fg="red", text="Password is incorrect")
                return
    login_notif.config(fg="red", text="Account not found")

def deopsit():
print("deposit")


def withdraw():
    print('withdraw')

def personal_details():
    #variables
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user.details[0]
    details_age = user.detail[2]
    details_gender = user.details[3]
    details_balance = user.detail[4]
    #Personal Details Screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    print('personal detials')
    #Labels
    Label(personal_details_screen, text="Personal Details", font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text="Name : "+details_name, font=('Calibri', 12)).grid(row=1, sticky=W, pady=10)
    Label(personal_details_screen, text="Age : "+details_age, font=('Calibri', 12)).grid(row=2, sticky=W, pady=10)
    Label(personal_details_screen, text="Gender : "+details_gender, font=('Calibri', 12)).grid(row=3, sticky=W, pady=10)
    Label(personal_details_screen, text="Balance : £"+details_balance, font=('Calibri', 12)).grid(row=4, sticky=W, pady=10)
    
def login():
    #Variables
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StinrgVar()
    temp_login_password = StinrgVar()
    #Login Screen
    login_screen = TopLevel(master)
    login_screen.title("Login")
    Label(login_screen, text="Login to your account", font=('Calibri',12)).grid(row=0, sticky=N, pady10)
    Label(login_screen, text="Username", font=('Calibri',12)).grid(row=1, sticky=W)
    Label(login_screen, text="Password", font=('Calibri',12)).grid(row=2, sticky=W)
    login_notif = Label(login_screen, font=('Calibri', 12))
    login_notif.grid(row=4, sticky=N)

    #Entries
    Entry(login_screen, text_variable=temp_login_name).grid(row=1, column=1, padx=5)
    Entry(login_screen, text_variable=temp_login_password, show="*").grid(row=2, column=1, padx=5)

    #Buttons
    Button(login_screen text="Login", font('Calibiri', 12), width=20, command=login_session).grid(row=3, sticky=W, pady=5, padx=5)



#Image Import
img = Image.open("currency.jpg")
img = img.resize((150, 150))
img = Image.Tk.PhotoImage(img)

#Lables
Label(master, text="Custom Banking Beta", font=('Calibri', 14)).grid(row=0, sticky=N, pady=10)
Label(master, text="Secure Banking online", font=('Calibri', 12)).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2, sticky=N, pady=15)

#Buttons
Button(master, text="Register", font('Calibiri', 12), width=20, command=register).grid(row=3, sticky=N)
Button(master, text="Login", font('Calibiri', 12), width=20, command=login).grid(row=4, sticky=N, pady=10)
#added so application can stay in a loop and does not crash
master.mainloop()
