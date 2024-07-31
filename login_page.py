from tkinter import *
from tkinter import messagebox
from PIL import Image
import customtkinter
from customtkinter import *
import mysql.connector

# Local database connection
db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd=" ",
	database=" "
)

# Cursor
mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE InventoryManagement") 

# Tables
#mycursor.execute("CREATE TABLE Equipment (id int PRIMARY KEY AUTO_INCREMENT, code VARCHAR(), serial_number VARCHAR(), name VARCHR(), model VARCHAR(), department VARCHAR(), place VARCHAR(), manufacturer VARCHAR(), manufacture_date DATE, purchase_date DATE, install_date DATE, operation_condition enum('Working', 'Not working'), calibration VARCHAR(), calibration_date DATE, cost int(), supplier VARCHAR())")
#mycursor.execute("CREATE TABLE Tools (id int(), type VARCHAR(), manufacturer VARCHAR(),manu_date, expiration_date DATE, location VARCHAR())
#mycursor.execute("CREATE TABLE Furniture (id int(), code_identifier VARCHAR(), type VACHAR() PRIMARY KEY, location VARCHAR(), installation_date()")
#mycursor.execute("CREATE TABLE Users (username VARCHAR(50) NOT NULL,  password VARCHAR(50) NOT NULL, email VARCHAR(60) NOT NULL)")
#mycursor.execute("CREATE TABLE Maintenance (id int PRIMARY KEY, fault_id int, fault_type LONGTEXT, proposed_maintenance LONGTEXT, cost int, last_maintenance DATE, preventive_maintenance DATE, fault_description LONGTEXT)")

# Functions
def signup_page():
    login.destroy()
    import signup_page

#def user_enter(event):
    #if Username.get()=='اسم المستخدم':
        #Username.delete(0,END)
#def pass_enter(event):
    #if Password.get()=='كلمة المرور':
        #Password.delete(0,END) 

def login_user():
    if Username.get()=='' or Password.get()=='':
        messagebox.showerror('خطأ', 'يجب ملء كل الحقول')
    else:
        select_query="SELECT * FROM users WHERE username=%s AND password=%s "
        mycursor.execute(select_query, (Username.get(), Password.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('خطأ','اسم المستخدم او كلمة المرور خطأ')
        else:
            messagebox.showinfo('نجاح','مرحبا')
            login.destroy()
            import app_test
            
#def hide():
    #openeye.config(file='closeye.png')
    #Password.config(show='*')
    #eyeBttn.config(command=show)
#def show():
    #openeye.config(file='openeye.png')
    #Password.config(show='')
    #eyeBttn.config(command=hide)

# Login page
#def login_page():
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
login = CTk()

firstimage=customtkinter.CTkImage(light_image= Image.open("bgs.png"), size=(610,580))
imageLabel=customtkinter.CTkButton(login, image=firstimage, width=0, height=0, text="", border_spacing=0, border_width=0, fg_color='#447b9c', state='unclickable').place(x=0, y=0)
#Main=PhotoImage(file='main.png')
#imageLabel=customtkinter.CTkLabel(login, image=Main).place(x=0, y=320)
#imageLabel.grid(row=0, column=0)
login.resizable(0,0)
login.title("Login Page")
login.geometry("990x580")

heading=customtkinter.CTkLabel(login, text="دخول تسجيل", font=('Microsoft Yahei UI Light', 23, 'bold')) 
heading.place(x=750, y=50)

Username= customtkinter.CTkEntry(login, placeholder_text="اسم المستخدم",width=230, font=('Microsoftt Yahei UI Light', 13, 'bold'))
Username.place(x=690, y=200)
#Username.insert(0, 'اسم المستخدم')
#Username.bind('<FocusIn>', user_enter)

Password= customtkinter.CTkEntry(login,placeholder_text="كلمة المرور", width=230, font=('Microsoftt Yahei UI Light', 13, 'bold'))
Password.place(x=690, y=300)
#Password.configure(show='*')
#Password.insert(0, 'كلمة المرور')
#Password.bind('<FocusIn>', command=pass_enter)

#openeye=PhotoImage(file='openeye.png')
#eyeBttn=customtkinter.CTkButton(login, image=openeye, bd=0, bg='#84839C', activebackground='#84839C', cursor='hand2', command=hide).place(x=895, y=290)

# Forgot password button

# Login button
loginBttn=customtkinter.CTkButton(login, text='تسجيل دخول', font=('Open Sans', 16, 'bold'), cursor='hand2', width=19, command=login_user).place(x=760, y=400)

orlabel=customtkinter.CTkLabel(login, text='------------- او -------------', font=('Open Sans', 13)).place(x=730, y=455)

signupBttn=customtkinter.CTkButton(login, text='انشاء حساب جديد', font=('Open Sans', 16), cursor='hand2', width=19, command=signup_page).place(x=750, y=500)

login.mainloop()