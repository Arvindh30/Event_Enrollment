import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Arvindh#01',  
        db='event_db',
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=10, column=1, columnspan=5, rowspan=11, padx=70, pady=20)

def setph(word, num):
    if num == 1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
        ph3.set(word)
    if num == 4:
        ph4.set(word)
    if num == 5:
        ph5.set(word)
    if num == 6:
        ph6.set(word)
    if num == 7:
        ph7.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stuevent")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    studid = str(studidEntry.get())
    name = str(nameEntry.get())
    dept = str(deptEntry.get())
    year = str(yearEntry.get())
    phone = str(phoneEntry.get())
    hostel = str(hostelEntry.get())
    event = str(eventEntry.get())

    if (studid == "" or studid == " ") or (name == "" or name == " ") or (dept == "" or dept == " ") or (year == "" or year == " ") or (phone == "" or phone == " ") or (hostel == "" or hostel == " ") or (event == "" or event == " "):
        messagebox.showinfo("Error !!", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO stuevent VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (studid, name, dept, year, phone, hostel, event))
            conn.commit()
            conn.close()
        except pymysql.err.IntegrityError:
            messagebox.showinfo("Error !!", "Student ID already exists")
            return

    refreshTable()

def reset():
    
    studidEntry.delete(0, "end")
    nameEntry.delete(0, "end")
    deptEntry.delete(0, "end")
    yearEntry.delete(0, "end")
    phoneEntry.delete(0, "end")
    hostelEntry.delete(0, "end")
    eventEntry.delete(0, "end")

def delete():
    studid = str(studidEntry.get())

    conn = connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM stuevent WHERE STUDENT_ID=%s ;", (studid,))
        conn.commit()
        conn.close()

    except Exception as e:
        messagebox.showinfo("Error !!", "No data found")

    refreshTable()
    

def select():
    try:
        selected_item = my_tree.selection()[0]
        studid = str(my_tree.item(selected_item)['values'][0])
        name = str(my_tree.item(selected_item)['values'][1])
        dept = str(my_tree.item(selected_item)['values'][2])
        year = str(my_tree.item(selected_item)['values'][3])
        phone = str(my_tree.item(selected_item)['values'][4])
        hostel = str(my_tree.item(selected_item)['values'][5])
        event = str(my_tree.item(selected_item)['values'][6])

        setph(studid, 1)
        setph(name, 2)
        setph(dept, 3)
        setph(year, 4)
        setph(phone, 5)
        setph(hostel, 6)
        setph(event, 7)

    except IndexError:
        messagebox.showinfo("Error", "Please select a data row")

def search():
    studid = str(studidEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stuevent WHERE STUDENT_ID=%s ",
                   (studid))

    try:
        result = cursor.fetchall()

        for num in range(0, 7):
            setph(result[0][num], (num + 1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error !!", "No data found")

def update():

    studid = str(studidEntry.get())
    name = str(nameEntry.get())
    dept = str(deptEntry.get())
    year = str(yearEntry.get())
    phone = str(phoneEntry.get())
    hostel = str(hostelEntry.get())
    event = str(eventEntry.get())

    if (studid == "" or studid == " ") or (name == "" or name == " ") or (dept == "" or dept == " ") or (
            year == "" or year == " ") or (phone == "" or phone == " ") or (hostel == "" or hostel == " ") or (event == "" or event == " "):
        messagebox.showinfo("Error !!", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE stuevent SET NAME=%s, DEPARTMENT=%s, YEAR=%s, PHONE=%s, HOSTEL=%s, EVENT=%s WHERE STUDENT_ID=%s",
                           (name, dept, year, phone, hostel, event,studid))
            conn.commit()
            conn.close()
        except pymysql.err.IntegrityError:
            messagebox.showinfo("Error !!", "Student ID Not exists")
            return

    refreshTable()

root = tk.Tk()
root.title("Event Registration System")
root.geometry("1920x1080")
my_tree = ttk.Treeview(root)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))
root.tk.call("source",r"d:\Projects\Event Enrollment\forest-light.tcl")
style.theme_use("forest-light")

ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()
ph6 = tk.StringVar()
ph7 = tk.StringVar()

label = Label(root, text="                    Event Registration System", font=('Arial Bold', 30))
label.grid(row=0, column=1, columnspan=8, rowspan=2, padx=50, pady=40)

studidLabel = ttk.Label(root, text="Student ID       :", font=('Arial', 15))
nameLabel = ttk.Label(root, text="Name              :", font=('Arial', 15))
deptLabel = ttk.Label(root, text="Department     :", font=('Arial', 15))
yearLabel = ttk.Label(root, text="Year               :", font=('Arial', 15))
phoneLabel = ttk.Label(root, text="Phone             :", font=('Arial', 15))
hostelLabel = ttk.Label(root, text="Hostel             :", font=('Arial', 15))
eventLabel = ttk.Label(root, text="Event              :", font=('Arial', 15))

studidLabel.grid(row=3, column=1, columnspan=1, padx=50, pady=5)
nameLabel.grid(row=4, column=1, columnspan=1, padx=50, pady=5)
deptLabel.grid(row=5, column=1, columnspan=1, padx=50, pady=5)
yearLabel.grid(row=6, column=1, columnspan=1, padx=50, pady=5)
phoneLabel.grid(row=7, column=1, columnspan=1, padx=50, pady=5)
hostelLabel.grid(row=8, column=1, columnspan=1, padx=50, pady=5)
eventLabel.grid(row=9, column=1, columnspan=1, padx=50, pady=5)

studidEntry = ttk.Entry(root, width=55, font=('Arial', 15), textvariable = ph1)
nameEntry = ttk.Entry(root, width=55, font=('Arial', 15), textvariable = ph2)
deptEntry =  ttk.Entry(root, width=55, font=('Arial', 15), textvariable = ph3) 
yearEntry = ttk.Entry(root, width=55, font=('Arial', 15), textvariable = ph4)
phoneEntry = ttk.Entry(root, width=55, font=('Arial', 15), textvariable = ph5)
hostelEntry = ttk.Entry(root, width=55, font=('Arial', 15), textvariable = ph6)
eventEntry = ttk.Combobox(root, width=54, values=["Yoga","Web Dev","Cyber Security","Internet of Things"], font=('Arial', 15), textvariable = ph7)

studidEntry.grid(row=3, column=2, columnspan=4, padx=70, pady=5)
nameEntry.grid(row=4, column=2, columnspan=4, padx=70, pady=5)
deptEntry.grid(row=5, column=2, columnspan=4, padx=70, pady=5)
yearEntry.grid(row=6, column=2, columnspan=4, padx=70, pady=5)
phoneEntry.grid(row=7, column=2, columnspan=4, padx=70, pady=5)
hostelEntry.grid(row=8, column=2, columnspan=4, padx=70, pady=5)
eventEntry.grid(row=9, column=2, columnspan=4, padx=70, pady=5)

addBtn = Button(
    root, text="Add", padx=65, pady=25, width=10,command=add)
updateBtn = Button(
    root, text="Update", padx=65, pady=25, width=10,command=update)
deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=10,command=delete)
searchBtn = Button(
    root, text="Search", padx=65, pady=25, width=10,command=search)
resetBtn = Button(
    root, text="Reset", padx=65, pady=25, width=10,command=reset)
selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=10,command=select)

addBtn.grid(row=3, column=8, columnspan=1, rowspan=2,pady=5)
updateBtn.grid(row=5, column=8, columnspan=1, rowspan=2,pady=5)
deleteBtn.grid(row=7, column=8, columnspan=1, rowspan=2,pady=5)
searchBtn.grid(row=9, column=8, columnspan=1, rowspan=2,pady=5)
resetBtn.grid(row=11, column=8, columnspan=1, rowspan=2,pady=15)
selectBtn.grid(row=13, column=8, columnspan=1, rowspan=2,pady=15)


my_tree['columns'] = ("Student ID","Name","Department","Year","Phone","Hostel","Event")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Student ID", anchor=W, width=130)
my_tree.column("Name", anchor=W, width=130)
my_tree.column("Department", anchor=W, width=160)
my_tree.column("Year", anchor=W, width=80)
my_tree.column("Phone", anchor=W, width=130)
my_tree.column("Hostel", anchor=W, width=150)
my_tree.column("Event", anchor=W, width=165)


my_tree.heading("Student ID", text="Student ID", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Department", text="Department", anchor=W)
my_tree.heading("Year", text="Year", anchor=W)
my_tree.heading("Phone", text="Phone", anchor=W)
my_tree.heading("Hostel", text="Hostel", anchor=W)
my_tree.heading("Event", text="Event", anchor=W)

refreshTable()

root.mainloop()