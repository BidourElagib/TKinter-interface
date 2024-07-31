import customtkinter
from customtkinter import *
import mysql.connector
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

# Local database connection
db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd=" ",
	database=" "
)

# Create cursor
mycursor = db.cursor()

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

Main = CTk()
Main.resizable(0,0)
Main.title("Main Page")
Main.geometry("990x580")
Main.config()

# Treeview styling 
style=ttk.Style()
style.theme_use("default")
style.configure("Treeview", background='white', foreground='black', rowheight=30, fieldbackground='white') ##C4C4C4 is for gray

style.map('Treeview', background=[('selected', '#0E4D92')])
    
# Frames
def menu_page():
    menu_page= customtkinter.CTkFrame(main_frame, width=990, height=550, fg_color='white').place(x=0, y=50)

    def add_equip():
        query="INSERT INTO equipment (code, serial_number, name, model, department, place, manufacturer, manufacture_date, purchase_date, install_date, operation_condition, calibration, calibration_date, cost, supplier) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(query, (code_entry.get(), serial_entry.get(), name_entry.get(), model_entry.get(), dept_entry.get(), place_entry.get(), manuf_entry.get(), purchase_entry.get(), install_entry.get(), condition_entry.get(), calibration_entry.get(), calidate_entry.get(), cost_entry.get(), supplier_entry.get()))

        db.commit()

    def add_tool():
        query="INSERT INTO tools (code, serial_number, name, model, department, place, manufacturer, manufacture_date, purchase_date, install_date, operation_condition, calibration, calibration_date, cost, supplier) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(query, (code_entry.get(), serial_entry.get(), name_entry.get(), model_entry.get(), dept_entry.get(), place_entry.get(), manuf_entry.get(), purchase_entry.get(), install_entry.get(), condition_entry.get(), calibration_entry.get(), calidate_entry.get(), cost_entry.get(), supplier_entry.get()))

        db.commit()

    def add_furniture():
        query="INSERT INTO furniture (code, serial_number, name, model, department, place, manufacturer, manufacture_date, purchase_date, install_date, operation_condition, calibration, calibration_date, cost, supplier) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(query, (code_entry.get(), serial_entry.get(), name_entry.get(), model_entry.get(), dept_entry.get(), place_entry.get(), manuf_entry.get(), purchase_entry.get(), install_entry.get(), condition_entry.get(), calibration_entry.get(), calidate_entry.get(), cost_entry.get(), supplier_entry.get()))

        db.commit()

    tabview = customtkinter.CTkTabview(menu_page, width=990, height=580)
    tabview.place(x=0, y=40)

    tabview.add("طبية اجهزة")
    tabview.add("ادوات")
    tabview.add("اثاثات")

#Equipment
    code=customtkinter.CTkLabel(tabview.tab("طبية اجهزة"), text='Item code: ').place(x=40, y=100)
    code_entry=customtkinter.CTkEntry(tabview.tab("طبية اجهزة"), width=100).place(x=110, y=100)

    serial=customtkinter.CTkLabel(tabview.tab("طبية اجهزة"), text='Serial Number: ').place(x=40, y=130)
    serial_entry=customtkinter.CTkEntry(tabview.tab("طبية اجهزة"), width=100).place(x=140, y=130)

    name=customtkinter.CTkLabel(tabview.tab("طبية اجهزة"), text='Item Name: ').place(x=40, y=160)
    name_entry=customtkinter.CTkEntry(tabview.tab("طبية اجهزة"), width=100).place(x=120, y=160)

    model=customtkinter.CTkLabel(tabview.tab("طبية اجهزة"), text='Model: ').place(x=40, y=190)
    model_entry=customtkinter.CTkEntry(tabview.tab("طبية اجهزة"), width=100).place(x=90, y=190)

    dept=customtkinter.CTkLabel(tabview.tab("طبية اجهزة"), text='Department: ').place(x=40, y=220)
    dept_entry=customtkinter.CTkEntry(tabview.tab("طبية اجهزة"), width=100).place(x=120, y=220)

    place=customtkinter.CTkLabel(tabview.tab("طبية اجهزة"), text='place: ').place(x=40, y=250)
    place_entry=customtkinter.CTkEntry(tabview.tab("طبية اجهزة"), width=100).place(x=90, y=250)

    manuf=customtkinter.CTkLabel(tabview.tab("طبية اجهزة"), text='Manufacturer: ').place(x=40, y=280)
    manuf_entry=customtkinter.CTkEntry(tabview.tab("طبية اجهزة"), width=100).place(x=130, y=280)

    purchase=customtkinter.CTkLabel(tabview.tab("طبية اجهزة"), text='Purchase Date: ').place(x=40, y=190)
    purchase_entry=customtkinter.CTkEntry(tabview.tab("طبية اجهزة"), width=100).place(x=140, y=190)

    install=customtkinter.CTkLabel(tabview.tab("طبية اجهزة"), text='Install Date: ').place(x=350, y=100)
    install_entry=customtkinter.CTkEntry(tabview.tab("طبية اجهزة"), width=100).place(x=430, y=100)

    condition=customtkinter.CTkLabel(tabview.tab("طبية اجهزة"), text='Operation Condition: ').place(x=350, y=130)
    condition_entry=customtkinter.CTkOptionMenu(tabview.tab("طبية اجهزة"), width=100, values=("Working", "Not Working")).place(x=480, y=130)

    calibration=customtkinter.CTkLabel(tabview.tab("طبية اجهزة"), text='Calibration: ').place(x=350, y=160)
    calibration_entry=customtkinter.CTkEntry(tabview.tab("طبية اجهزة"), width=100).place(x=420, y=160)

    cali_date=customtkinter.CTkLabel(tabview.tab("طبية اجهزة"), text='Calibration Date: ').place(x=350, y=190)
    calidate_entry=customtkinter.CTkEntry(tabview.tab("طبية اجهزة"), width=100).place(x=460, y=190)

    cost=customtkinter.CTkLabel(tabview.tab("طبية اجهزة"), text='Cost: ').place(x=350, y=220)
    cost_entry=customtkinter.CTkEntry(tabview.tab("طبية اجهزة"), width=100).place(x=460, y=220)

    supplier=customtkinter.CTkLabel(tabview.tab("طبية اجهزة"), text='Supplier: ').place(x=350, y=250)
    supplier_entry=customtkinter.CTkEntry(tabview.tab("طبية اجهزة"), width=100).place(x=460, y=250)

    add_button=CTkButton(tabview.tab("طبية اجهزة"), text='الجهاز اضف', command=add_equip).place(x=40, y=415)

#Tools
    ttype=customtkinter.CTkLabel(tabview.tab("Tool"), text='Type: ').place(x=40, y=100)
    ttype_entry=customtkinter.CTkEntry(tabview.tab("Tool"), width=100).place(x=110, y=100)

    tmanu=customtkinter.CTkLabel(tabview.tab("Tool"), text='Manufacturer: ').place(x=40, y=130)
    tmanu_entry=customtkinter.CTkEntry(tabview.tab("Tool"), width=100).place(x=140, y=130)

    texp=customtkinter.CTkLabel(tabview.tab("Tool"), text='Expiration Date: ').place(x=40, y=160)
    texp_entry=customtkinter.CTkEntry(tabview.tab("Tool"), width=100).place(x=120, y=160)

    tplace=customtkinter.CTkLabel(tabview.tab("Tool"), text='place/room: ').place(x=40, y=190)
    tplace_entry=customtkinter.CTkEntry(tabview.tab("Tool"), width=100).place(x=90, y=190)

    cused=customtkinter.CTkLabel(tabview.tab("Tool"), text='Currently Used: ').place(x=40, y=220)
    cused_entry=customtkinter.CTkEntry(tabview.tab("Tool"), width=100).place(x=90, y=220)

    cstored=customtkinter.CTkLabel(tabview.tab("Tool"), text='Currently Stored: ').place(x=40, y=250)
    cstored_entry=customtkinter.CTkEntry(tabview.tab("Tool"), width=100).place(x=90, y=250)

    costpb=customtkinter.CTkLabel(tabview.tab("Tool"), text='Cost Per Batch: ').place(x=40, y=280)
    costpb_entry=customtkinter.CTkEntry(tabview.tab("Tool"), width=100).place(x=90, y=280)

    tadd_button=CTkButton(tabview.tab("Tool"), text='Add Tool', command=add_tool).place(x=40, y=415)

#Furniture
    fcode=customtkinter.CTkLabel(tabview.tab("Furniture"), text='Code: ').place(x=40, y=100)
    fcode_entry=customtkinter.CTkEntry(tabview.tab("Furniture"), width=100).place(x=110, y=100)

    ftype=customtkinter.CTkLabel(tabview.tab("Furniture"), text='Type: ').place(x=40, y=130)
    ftype_entry=customtkinter.CTkEntry(tabview.tab("Furniture"), width=100).place(x=140, y=130)

    fdept=customtkinter.CTkLabel(tabview.tab("Furniture"), text='Department: ').place(x=40, y=160)
    fdept_entry=customtkinter.CTkEntry(tabview.tab("Furniture"), width=100).place(x=120, y=160)

    flocation=customtkinter.CTkLabel(tabview.tab("Furniture"), text='Location: ').place(x=40, y=190)
    flocation_entry=customtkinter.CTkEntry(tabview.tab("Furniture"), width=100).place(x=90, y=190)

    fnum=customtkinter.CTkLabel(tabview.tab("Furniture"), text='Number of Items: ').place(x=40, y=220)
    fnum_entry=customtkinter.CTkEntry(tabview.tab("Furniture"), width=100).place(x=90, y=220)

    fadd_button=CTkButton(tabview.tab("Furniture"), text='Add Furniture', command=add_tool).place(x=40, y=415)

def search_page():
    search_page= customtkinter.CTkFrame(main_frame, width=990, height=550, fg_color='white').place(x=0, y=50)

    cmb=customtkinter.CTkComboBox(search_page, values=["اجهزة", "ادوات", "اثاثات", "مستخدمين"]).place(x=350, y=80)

    Search=customtkinter.CTkLabel(search_page, text='الجهاز ادخل اسم').place(x=50, y=80)
    search_entry=customtkinter.CTkEntry(search_page, width=200).place(x=130, y=80)

# Creating tree
    tree=ttk.Treeview(search_page, selectmode='extended')

# Columns
    tree['columns']=("Username", "Password", "Email")

# Add these in the loops and adjust according to the columns
    tree.column("#0", width=0, minwidth=0)
    tree.column("Username", anchor=W, width=300)
    tree.column("Password", anchor=W, width=300)
    tree.column("Email", anchor=W, width=400)

# Headings
    tree.heading("Username", text="Username", anchor=W)
    tree.heading("Password", text="Password", anchor=W)
    tree.heading("Email", text="Email Address", anchor=W)

# Displaying data from database
    def display():
        tree.tag_configure('oddrow', background="white")
        tree.tag_configure('evenrow', background="lightblue")

        mycursor.execute("SELECT * FROM users")
        rows=mycursor.fetchall()
        i=0
        for record in rows:
            if i % 2 ==0:
                tree.insert(parent='', index='end', iid=i, tags=('evenrow'), text="", values=(record[0], record[1],record[2]))
            else:
                tree.insert(parent='', index='end', iid=i, tags=('oddrow'), text="", values=(record[0], record[1],record[2]))
            i += 1
        # Fix the Loops
        # else:
        #     query="SELECT * FROM users WHERE username=%s OR email=%s" 
        #     mycursor.execute(query, (search_entry.get()))

        #     rows=mycursor.fetchall()
        #     i=0
        #     for records in rows:
        #         tree.insert(parent='', index='end', iid=i, text="", values=(record[0], record[1],record[2]))
        #     i= i+1

        # if cmb.get() == "Users": 
        #     if search_entry.get() == None:
        #         mycursor.execute("SELECT * FROM users")
        #         rows=mycursor.fetchall()
        #         i=0
        #         for record in rows:
        #             if i % 2 ==0:
        #                 tree.insert(parent='', index='end', iid=i, tags=('evenrow'), text="", values=(record[0], record[1],record[2]))
        #             else:
        #                 tree.insert(parent='', index='end', iid=i, tags=('oddrow'), text="", values=(record[0], record[1],record[2]))
        #             i += 1
        #     else:
        #         query="SELECT * FROM users WHERE username=%s OR email=%s" 
        #         mycursor.execute(query, (search_entry.get(), search_entry.get()))

        #         rows=mycursor.fetchone()
        #         tree.insert(parent='', index='end', iid=i, text="", values=(rows))

        # elif cmb.get() == "Equipment":
        #     if search_entry.get() == None:
        #         mycursor.execute("SELECT * FROM equipment")

        #         rows=mycursor.fetchall()
        #         i=0
        #         for record in rows:
        #             if i % 2 ==0:
        #                 tree.insert(parent='', index='end', iid=i, tags=('evenrow'), text="", values=(record[0], record[1],record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9],record[10], record[11], record[12], record[13], record[14]))
        #             else:
        #                 tree.insert(parent='', index='end', iid=i, tags=('oddrow'), text="", values=(record[0], record[1],record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9],record[10], record[11], record[12], record[13], record[14]))
        #             i += 1

        #     else:
        #         query="SELECT * FROM equipment WHERE id=%s OR code=%s OR serial_number=%s OR name=%s OR model=%s OR department=%s OR place=%s OR manufacturer=%s OR manufacturer_date=%s OR purchase_date=%s OR install_date=%s OR operation_condition=%sOR calibration=%s OR calibration_date=%s OR cost=%s OR supplier=%s"
        #         mycursor.execute(query, (search_entry.get()))
        #         rows=mycursor.fetchall()

        #         i=0
        #         for record in rows:
        #             if i % 2 ==0:
        #                 tree.insert(parent='', index='end', iid=i, tags=('evenrow'), text="", values=(record[0], record[1],record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9],record[10], record[11], record[12], record[13], record[14]))
        #             else:
        #                 tree.insert(parent='', index='end', iid=i, tags=('oddrow'), text="", values=(record[0], record[1],record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9],record[10], record[11], record[12], record[13], record[14]))
        #             i += 1

        # elif cmb.get() == "Tools":
        #     if search_entry.get() == None:
        #         mycursor.execute("SELECT * FROM tools")
        #         rows=mycursor.fetchall()
        #         i=0
        #         for record in rows:
        #             tree.insert(parent='', index='end', iid=i, text="", values=()) #add values depending on columns in table
        #             i +=1
        #     else:
        #         query="SELECT * FROM tools WHERE name=% " #adjust depending on searchable columns
        #         mycursor.execute(query, (search_entry.get()))
        #         rows=mycursor.fetchone()
        #         tree.insert(parent='', index='end', iid=i, text="", values=(rows))

        # elif cmb.get() == "Furniture":
        #     if search_entry.get() == None:
        #         mycursor.execute("SELECT * FROM furniture")
        #         rows=mycursor.fetchall()
        #         i=0
        #         for record in rows:
        #             tree.insert(parent='', index='end', iid=i, text="", values=()) #add values depending on columns in table
        #             i +=1
        #     else:
        #         query="SELECT * FROM furniture WHERE id=%" #adjust depending on searchable columns
        #         mycursor.execute(query, (search_entry.get()))
        #         rows=mycursor.fetchone()
        #         tree.insert(parent='', index='end', iid=i, text="", values=(rows)) #add values depending on columns in table           
        # else:
        #     messagebox.showerror('Error', 'please select a type')

    tree.place(x=70, y=250)

# Binding
    tree.bind("<Double-1>")

    #deleting selected one or all rows
    #Bind to database
    def delete_row():
        selected_rows= tree.selection()
        for record in selected_rows:
            tree.delete(record)

    def delete_all():
        for record in tree.get_children():
            tree.delete(record)

# Updating rows
    def update_row():
        pass
    
    def select_row():
        pass

    upd_button=CTkButton(search_page, text='تعديل', command=update_row).place(x=50, y=500)

    del_button=CTkButton(search_page, text='مسح', command=delete_row, fg_color='red').place(x=210, y=500)
    del_all=CTkButton(search_page, text='الكل مسح', fg_color="red", command=delete_all).place(x=370, y=500)

    search_button=customtkinter.CTkButton(search_page, text='بحث', command=display).place(x=50, y=120)

def faults_page():
    faults_page= customtkinter.CTkFrame(main_frame, width=990, height=550, fg_color='white').place(x=0, y=50)
    
# Add fault opens a new window 
    def add_fault():
        global fault
        fault=CTk()
        fault.title('ADD FAULT')
        fault.geometry("500x500")

        fault.mainloop()

# Treeview
    tree=ttk.Treeview(faults_page, selectmode='extended')

    tree['columns']=("id", "fault id", "fault type", "proposed maintenance", "cost", "last maintenance", "preventive maintenance", "fault desrciption")

    tree.column("#0", width=0, minwidth=0)
    tree.column("id", anchor=W, width=50)
    tree.column("fault id", anchor=W, width=50)
    tree.column("fault type", anchor=W, width=200)
    tree.column("proposed maintenance", anchor=W, width=200)
    tree.column("cost", width=0, minwidth=50)
    tree.column("last maintenance", anchor=W, width=200)
    tree.column("preventive maintenance", anchor=W, width=200)
    tree.column("fault desrciption", anchor=W, width=300)

    tree.heading("id", text="ID", anchor=W)
    tree.heading("fault id", text="Fault ID", anchor=W)
    tree.heading("fault type", text="Fault Type", anchor=W)
    tree.heading("proposed maintenance", text="Proposed Maintenance", anchor=W)
    tree.heading("cost", text="Cost", anchor=W)
    tree.heading("last maintenance", text="Last Maintenance", anchor=W)
    tree.heading("preventive maintenance", text="Preventive Maintenance", anchor=W)
    tree.heading("fault desrciption", text="Fault Description", anchor=W)

# Check to see if we need to add this inside the loop
    tree.tag_configure('oddrow', background="white")
    tree.tag_configure('evenrow', background="lightblue")

    mycursor.execute("SELECT * FROM Maintenance")
    rows=mycursor.fetchall()
    i=0

    for record in rows:
        if i % 2 ==0:
            tree.insert(parent='', index='end', iid=i, tags=('evenrow'), text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]))
        else:
            tree.insert(parent='', index='end', iid=i, tags=('oddrow'), text="", values=(record[0], record[1],record[2], record[3], record[4], record[5], record[6], record[7]))
        i += 1
    
    tree.place(x=70, y=250)

    def display_specific():
        tree.tag_configure('oddrow', background="white")
        tree.tag_configure('evenrow', background="lightblue")
        
        query="SELECT * FROM Maintenance WHERE id=%s OR fault_id=%s OR fault_type=%s OR proposed_maintenance=%s OR cost=%s OR last_maintenance=%s OR preventive_+maintenance=%s OR fault_description=%s"
        mycursor.execute(query, (fault_search.get()))
# Check if i have to add it 9 times or just once
        myrows=mycursor.fetchall()
        i=0
        for record in myrows:
            if i % 2 ==0:
                tree.insert(parent='', index='end', iid=i, tags=('evenrow'), text="", values=(record[0], record[1],record[2], record[3], record[4], record[5], record[6], record[7]))
            else:
                tree.insert(parent='', index='end', iid=i, tags=('oddrow'), text="", values=(record[0], record[1],record[2], record[3], record[4], record[5], record[6], record[7]))
            i += 1
        
    f_search=customtkinter.CTkLabel(faults_page, text='الجهاز اسم ادخل').place(x=50, y=80)
    fault_search=customtkinter.CTkEntry(faults_page, width=200).place(x=130, y=80)
    fault_searchbttn=customtkinter.CTkButton(faults_page, text='بحث', command=display_specific).place(x=50, y=120)

    add_faultbttn=customtkinter.CTkButton(faults_page, text='عطل اضافة', command=add_fault).place(x=50, y=500)

# Binding
    tree.bind("<Double-1>")

def reports_page():
    reports_page= customtkinter.CTkFrame(main_frame, width=990, height=550, fg_color='white').place(x=0, y=50)

    CTkButton(reports_page, text='Get Report!').place(x=50, y=80)

#def delete_page():
    #for frame in main_frame.winfo_children():
        #frame.destroy()
    
def indicate (page):
    #delete_page()
    page()

Menu_frame= customtkinter.CTkFrame(Main, width=990, height=50).place(x=0, y=0)

main_frame= customtkinter.CTkFrame(Main, width=990, height=550).place(x=0, y=50)

# Main Buttons
button1= customtkinter.CTkButton(Menu_frame, text='اضافة', width=247.5, corner_radius=0, height=50, command=lambda: indicate(menu_page)).place(x=0,y=0)

button2= customtkinter.CTkButton(Menu_frame, text='بحث', width=247.5, corner_radius=0, height=50, command=lambda: indicate(search_page)).place(x=247.5,y=0)

button3= customtkinter.CTkButton(Menu_frame, text='اعطال', width=247.5, corner_radius=0, height=50, command=lambda: indicate(faults_page)).place(x=495,y=0)

button4= customtkinter.CTkButton(Menu_frame, text='تقارير', width=247.5, corner_radius=0, height=50, command=lambda: indicate(reports_page)).place(x=742.5,y=0)

Main.mainloop()