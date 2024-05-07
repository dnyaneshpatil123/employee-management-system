import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql


#======Overall UI===========#

win=tk.Tk()
win.geometry("1350x700+0+0")
win.title("Employee Management System")

title_label=tk.Label(win, text="Employee Management System", font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="lightgrey")
title_label.pack(side=tk.TOP, fill=tk.X)

detail_frame=tk.LabelFrame(win,text="Enter Details",font=("Arial",20),bd=12,relief=tk.GROOVE,bg='lightgrey')
detail_frame.place(x=20,y=90,width=420,height=575)

data_frame=tk.Frame(win, bd=12,bg="lightgrey",relief=tk.GROOVE)
data_frame.place(x=475,y=90,width=810,height=575)  


#=========Variables================#

idno =tk.StringVar()
name = tk.StringVar()
post = tk.StringVar ()
department = tk.StringVar()
joining = tk.StringVar ()
contact = tk.StringVar()
address = tk.StringVar()
gender =tk.StringVar()
dob =tk.StringVar()

search =tk.StringVar()


#======Entry===========#

idno_lbl = tk.Label(detail_frame, text="ID ", font=("Arial", 15), bg="lightgrey")
idno_lbl.grid(row=0, column=0,padx=2,pady=2)

idno_ent = tk.Entry(detail_frame,bd=7,font=("arial",15),textvariable=idno)
idno_ent.grid(row=0,column=1,padx=2,pady=2)

name_lbl= tk.Label(detail_frame, text="Name ",font=('Arial',15),bg="lightgrey")
name_lbl.grid(row =1,column= 0,padx =2,pady =2)

name_ent = tk.Entry(detail_frame,bd=7, font=("arial",15),textvariable=name)
name_ent.grid(row=1, column=1,padx=2,pady=2)

post_lbl = tk.Label(detail_frame, text="Post ", font=("Arial",15), bg="lightgrey")
post_lbl.grid(row=2,column=0, padx=2,pady=2)

post_ent = tk.Entry(detail_frame,bd=7,font=("arial",15),textvariable=post)
post_ent.grid(row=2,column=1,padx=2,pady=2)

department_lbl= tk.Label (detail_frame, text="Department ",font=("Arial", 15),bg="lightgrey")
department_lbl.grid(row=3, column=0,padx=2,pady=2)

department_ent = tk.Entry(detail_frame,bd=7, font=("arial", 15),textvariable=department)
department_ent.grid(row=3,column=1,padx=2,pady=2)

doj_lbl = tk.Label (detail_frame, text="Joining Date ",font=('Arial',15), bg="lightgrey")
doj_lbl.grid(row=4,column=0,padx=2,pady=2)

doj_ent = tk.Entry(detail_frame,bd =7,font= ("arial",15),textvariable=joining)
doj_ent.grid(row=4,column=1,padx=2,pady=2)

contact_lbl= tk.Label (detail_frame, text="Contact ",font=("Arial", 15),bg="lightgrey")
contact_lbl.grid(row=5, column=0,padx=2,pady=2)

contact_ent = tk.Entry(detail_frame,bd=7, font=("arial", 15),textvariable=contact)
contact_ent.grid(row=5,column=1,padx=2,pady=2)

address_lbl= tk.Label (detail_frame, text="Address ",font=("Arial", 15),bg="lightgrey")
address_lbl.grid(row=6, column=0,padx=2,pady=2)

address_ent = tk.Entry(detail_frame,bd=7, font=("arial", 15),textvariable=address)
address_ent.grid(row=6,column=1,padx=2,pady=2)

gender_lbl = tk.Label(detail_frame,text="Gender ", font=("Arial", 15), bg="lightgrey")
gender_lbl.grid(row=7,column=0,padx=2,pady=2)

gender_ent = ttk.Combobox(detail_frame, font=("Arial",15), state="readonly",textvariable=gender)
gender_ent['values'] = ("Male", "Female")
gender_ent.grid(row=7,column=1,padx=2,pady=2)

dob_lbl = tk.Label (detail_frame, text="D.O.B ",font=('Arial',15), bg="lightgrey")
dob_lbl.grid(row=8,column=0,padx=2,pady=2)

dob_ent = tk.Entry(detail_frame,bd =7,font= ("arial",15),textvariable=dob)
dob_ent.grid(row=8,column=1,padx=2,pady=2)



#===========Functions====================#

def fetch_data():
    conn = pymysql.connect(host = "localhost",user="root",passwd="",db="ems1")

    curr = conn.cursor()
    curr.execute("SELECT * FROM data")
    rows = curr.fetchall()
    if len(rows)!=0:
        employee_table.delete(*employee_table.get_children())
        for row in rows:
            employee_table.insert('', tk. END, values= row)
        conn.commit()
    conn.close()

def add_data():
    if idno.get()=="" or name.get()=="" or post.get()=="":  
        messagebox.showerror("Error!", "Please fill all the fields!")
    else:
        conn = pymysql.connect(host="localhost", user="root", password="", database="ems1")
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES (%s, %s, %s, %s, %s, %s, %s ,%s, %s)", (idno.get(), name.get(), post.get(), department.get(), joining.get(), contact.get(), address.get(), gender.get(), dob.get() ))
        conn.commit()
        conn.close()
        fetch_data()

def get_cursor(event):
    cursor_row = employee_table.focus()
    content = employee_table.item(cursor_row)
    row = content ['values']
    if row:
        idno.set(row[0] if len(row) > 0 else "")
        name.set(row[1] if len(row) > 1 else "")
        post.set(row[2] if len(row) > 2 else "")
        department.set(row[3] if len(row) > 3 else "")
        joining.set(row[4] if len(row) > 4 else "")
        contact.set(row[5] if len(row) > 5 else "")
        address.set(row[6] if len(row) > 6 else "")
        gender.set(row[7] if len(row) > 7 else "")
        dob.set(row[8] if len(row) > 8 else "")
    else:
        clear_data()

def clear_data():
    idno.set("")
    name.set("")
    post.set("")
    department.set("")
    joining.set("")
    contact.set("")
    address.set("")
    gender.set("")
    dob.set("")

def delete_data():
    selected_item = employee_table.selection() 
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a record to delete.")
        return
    
    confirmation = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?")
    if confirmation:
        conn = pymysql.connect(host="localhost", user="root", password="", database="ems1")
        cursor = conn.cursor()
        for item in selected_item:
            id_to_delete = employee_table.item(item, "values")[0] 
            cursor.execute("DELETE FROM data WHERE idno=%s", (id_to_delete,))
        conn.commit()
        conn.close()
        fetch_data()

def update_data():
    conn = pymysql.connect(host="localhost",user="root",password="",database="ems1")
    curr = conn.cursor()
    curr.execute("update data set name=%s, post=%s, department=%s, joining=%s, contact=%s, address=%s, gender=%s, dob=%s where idno=%s",(name.get(), post.get(), department.get(), joining.get(), contact.get(), address.get(), gender.get(), dob.get(), idno.get()))

    conn.commit()
    conn.close()
    fetch_data()
    clear_data()

def search_data():
    search_query = search_entry.get()
    if search_query == "":
        messagebox.showwarning("Warning", "Please enter a search query.")
        return

    conn = pymysql.connect(host="localhost", user="root", password="", database="ems1")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE idno LIKE '%{search_query}%' OR name LIKE '%{search_query}%' OR post LIKE '%{search_query}%' OR department LIKE '%{search_query}%' OR joining LIKE '%{search_query}%' OR contact LIKE '%{search_query}%' OR address LIKE '%{search_query}%' OR gender LIKE '%{search_query}%' OR dob LIKE '%{search_query}%'")
    rows = cursor.fetchall()
    if len(rows) != 0:
        employee_table.delete(*employee_table.get_children())
        for row in rows:
            employee_table.insert('', tk.END, values=row)
    else:
        messagebox.showinfo("Information", "No records found.")
    conn.close()


#======Buttons===========#

btn_frame = tk.Frame (detail_frame,bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=22,y=390,width=340,height=120)

add_btn = tk.Button(btn_frame,bg="lightgrey", text="Add", bd=7,font=("Arial", 13),width=15,command=add_data)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame,bg="lightgrey", text="Update", bd=7, font=("Arial", 13), width=15, command=update_data)
update_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn =tk.Button(btn_frame,bg ="lightgrey", text= "Delete", bd= 7,font= ("Arial", 13), width= 15, command=delete_data)
delete_btn.grid(row=1,column=0,padx=2,pady=2)

clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear",bd=7, font=("Arial", 13),width=15, command=clear_data)
clear_btn.grid(row=1, column=1,padx=3,pady=2)



#=========Search===================#

search_frame = tk.Frame(data_frame, bg="lightgrey", bd=1, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(search_frame, text="Search", bg="lightgrey", font=("Arial", 14))
search_lbl.grid(row=0, column=0, padx=12, pady=2)

search_entry = tk.Entry(search_frame, font=("Arial", 14), textvariable=search)
search_entry.grid(row=0, column=1, padx=12, pady=2)

search_btn = tk.Button(search_frame, text="Search", font=("Arial", 13), bd=9, width=14, bg="lightgrey", command=search_data)
search_btn.grid(row=0, column=2, padx=12, pady=2)

show_all_btn = tk.Button(search_frame, text="Show All", font=("Arial", 13), bd=9, width=14, bg="lightgrey", command=fetch_data)
show_all_btn.grid(row=0, column=3, padx=12, pady=2)

#=======Database Frame ============#

main_frame = tk.Frame(data_frame,bg="lightgrey",bd=11, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)


y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)


employee_table = ttk.Treeview(main_frame, columns= ("ID", "Name", "Post", "Department", "Joining Date", "Contact", "Address", "Gender", "D.O.B"),yscrollcommand= y_scroll.set, xscrollcommand= x_scroll.set)

y_scroll.config(command=employee_table.yview)
x_scroll.config(command=employee_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

employee_table.heading("ID", text="ID")
employee_table.heading("Name", text= "Name")
employee_table.heading("Post", text="Post")
employee_table.heading("Department", text="Department")
employee_table.heading("Joining Date", text="Joining Date")
employee_table.heading("Contact", text="Contact")
employee_table.heading("Address", text="Address")
employee_table.heading("Gender", text="Gender")
employee_table.heading("D.O.B", text="D.O.B")


employee_table['show']= 'headings'

employee_table.column("ID", width=100)
employee_table.column("Name", width=100)
employee_table.column("Post", width=150)
employee_table.column("Department", width=150)
employee_table.column("Joining Date", width=100)
employee_table.column("Contact", width=100)
employee_table.column("Address", width=150)
employee_table.column("Gender", width=100)
employee_table.column("D.O.B", width=100)

employee_table.pack(fill=tk.BOTH, expand=True)


fetch_data()

employee_table.bind("<ButtonRelease-1>", get_cursor)


win.mainloop()