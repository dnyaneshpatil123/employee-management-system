import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql



# =======================UI=====================================#

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    
    window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

win = tk.Tk()
win.title("Employee Management System")
center_window(win, 1350, 700)

BG_COLOR = "#f0f0f0"
FONT = ("Arial", 12)

main_frame = tk.Frame(win, bg=BG_COLOR)
main_frame.pack(fill=tk.BOTH, expand=True)

header_frame = tk.Frame(main_frame, bg="white", pady=20)
header_frame.pack(fill=tk.X)

title_label = tk.Label(header_frame, text="Employee Management System", font=("Arial", 24, "bold"), bg="white", padx=10)
title_label.pack()

detail_frame = tk.LabelFrame(main_frame, text="Enter Details", font=("Arial", 16, "bold"), bg=BG_COLOR, padx=20, pady=10)
detail_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

data_frame = tk.Frame(main_frame, bg=BG_COLOR, padx=20, pady=10)
data_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)



#=================Variables==================#

idno = tk.StringVar()
name = tk.StringVar()
post = tk.StringVar()
department = tk.StringVar()
joining = tk.StringVar()
contact = tk.StringVar()
address = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()
search = tk.StringVar()


labels = ["ID", "Name", "Post", "Department", "Joining Date", "Contact", "Address", "Gender", "D.O.B"]
entries = [idno, name, post, department, joining, contact, address, gender, dob]

for i, label_text in enumerate(labels):
    label = tk.Label(detail_frame, text=label_text, font=FONT, bg=BG_COLOR)
    label.grid(row=i, column=0, sticky="e", padx=5, pady=5)

    entry = tk.Entry(detail_frame, font=FONT, textvariable=entries[i])
    entry.grid(row=i, column=1, sticky="w", padx=5, pady=5)



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



# =====================Buttons===================================#

btn_frame = tk.Frame(detail_frame, bg=BG_COLOR)
btn_frame.grid(row=len(labels)+1, columnspan=2, pady=10)

btn_texts = ["Add", "Update", "Delete", "Clear"]
commands = [add_data, update_data, delete_data, clear_data]

for i, btn_text in enumerate(btn_texts):
    btn = tk.Button(btn_frame, text=btn_text, font=FONT, width=10, command=commands[i])
    btn.grid(row=0, column=i, padx=5)



#=============================Search and show all button=====================================#

search_frame = tk.Frame(data_frame, bg=BG_COLOR)
search_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

search_entry = tk.Entry(search_frame, font=FONT, textvariable=search)
search_entry.grid(row=0, column=0, padx=5, pady=5)

search_btn = tk.Button(search_frame, text="Search", font=FONT, width=10, command=search_data)
search_btn.grid(row=0, column=1, padx=5, pady=5)

show_all_btn = tk.Button(search_frame, text="Show All", font=FONT, width=10, command=fetch_data)
show_all_btn.grid(row=0, column=2, padx=5, pady=5)



#============================main database======================================#

table_frame = tk.Frame(data_frame, bg=BG_COLOR)
table_frame.pack(fill=tk.BOTH, expand=True)

columns = ("ID", "Name", "Post", "Department", "Joining Date", "Contact", "Address", "Gender", "D.O.B")
employee_table = ttk.Treeview(table_frame, columns=columns, show="headings")
employee_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)



# =================================scoll bar=================================#

vsb = ttk.Scrollbar(table_frame, orient="vertical", command=employee_table.yview)
vsb.pack(side=tk.RIGHT, fill='y')

hsb = ttk.Scrollbar(data_frame, orient="horizontal", command=employee_table.xview)
hsb.pack(side=tk.BOTTOM, fill='x')

employee_table.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

for col in columns:
    employee_table.heading(col, text=col)
    employee_table.column(col, width=100, anchor="center")

employee_table.bind("<ButtonRelease-1>", lambda event: get_cursor(event))

fetch_data()

win.mainloop()
