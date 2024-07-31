from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image
import customtkinter
from customtkinter import *

# Local database connection
db = mysql.connector.connect(
	host="localhost",
	user="root",

	passwd=" ",
	database=" "
)

# Create cursor
mycursor = db.cursor()

# Functions
def login_page():
    signup.destroy()
    import login_page

def signup_user():
    if Email.get()=='' or Username_entry.get()=='' or Password_entry.get()=='' or Confirm_entry.get()=='':
        messagebox.showerror('Error', '!يجب ملء كل الحقول')
    elif Password_entry.get() != Confirm_entry.get():
        messagebox.showerror('Error', '!كلمة المرور غير مطابقة')
    else:
        user=[(Username_entry.get())]
        
        query="SELECT * FROM users WHERE username=%s"
        mycursor.execute(query, (user))

        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror('Error', 'اسم المستخدم موجود!')
        else:
            insert_query="INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            mycursor.execute(insert_query, (Username_entry.get(), Email.get(), Password_entry.get()))
            db.commit()
            messagebox.showinfo('نجاح', 'تم التسجيل بنجاح!')

            Username_entry.delete(0,END)
            Email.delete(0,END)
            Password_entry.delete(0,END)
            Confirm_entry.delete(0,END)

            signup.destroy()
            import login_page

# Signup page
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
signup=CTk()

firstimage=customtkinter.CTkImage(light_image= Image.open("bgs.png"), size=(610,580))
imageLabel=customtkinter.CTkButton(signup, image=firstimage, width=0, height=0, text="", border_spacing=0, border_width=0, fg_color='#447b9c', state='unclickable').place(x=0, y=0)
#firstImage=ImageTk.PhotoImage(file='bg.png')
#imageLabel.grid(row=0, column=0)

signup.resizable(0,0)
signup.title("Sign Up Page")
signup.geometry("990x580")

heading=customtkinter.CTkLabel(signup, text="جديد حساب انشاء", font=('Microsoft Yahei UI Light', 23, 'bold')) 
heading.place(x=730, y=50)

Username_entry= customtkinter.CTkEntry(signup, width=230, placeholder_text="اسم المستخدم", font=('Microsoftt Yahei UI Light', 13, 'bold'))
Username_entry.place(x=690, y=200)
#Username_entry.insert(0, 'اسم المستخدم')
#Username_entry.bind('<FocusIn>', user_enter)

Email= customtkinter.CTkEntry(signup, width=230, placeholder_text="البريد الالكتروني", font=('Microsoftt Yahei UI Light', 13, 'bold'))
Email.place(x=690, y=250)
#Email.insert(0, 'البريد الالكتروني')
#Email.bind('<FocusIn>', email_enter)

Password_entry= customtkinter.CTkEntry(signup, width=230, placeholder_text="كلمة المرور", font=('Microsoftt Yahei UI Light', 13, 'bold'))
Password_entry.place(x=690, y=300)
#Password_entry.insert(0, 'كلمة المرور')
#Password_entry.bind('<FocusIn>', pass_enter)

Confirm_entry= customtkinter.CTkEntry(signup, width=230,placeholder_text="تأكيد كلمة المرور", font=('Microsoftt Yahei UI Light', 13, 'bold'))
Confirm_entry.place(x=690, y=350)
#Confirm_entry.insert(0, 'تأكيد كلمة المرور')
#Confirm_entry.bind('<FocusIn>', conf_enter)

signupBttn=customtkinter.CTkButton(signup, text='انشاء حساب', font=('Open Sans', 16, 'bold'), cursor='hand2', width=19, command=signup_user).place(x=760, y=420)

orlabel=customtkinter.CTkLabel(signup, text='------------- او -------------', font=('Open Sans', 13)).place(x=730, y=460)

existingBttn=customtkinter.CTkButton(signup, text='تسجيل دخول', font=('Open Sans', 16), width=19, command=login_page).place(x=760, y=500)

signup.mainloop()