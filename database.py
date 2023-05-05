import tkinter as tk
import tkinter.messagebox
import sqlite3 as sq

conn = sq.connect('db.db')

# 創建窗口
window = tk.Tk()
window.title("DATAbase")

tk.Label(window, text="table：").grid(row=0, column=0, padx=10, pady=10)
tk.Label(window, text="欄位：").grid(row=1, column=0, padx=10, pady=10)
tk.Label(window, text="數值：").grid(row=2, column=0, padx=10, pady=10)
tk.Label(window, text="sql：").grid(row=3, column=0, padx=10, pady=10)

entry1 = tk.Entry(window, width=9, justify="right", font=("Arial", 16))
entry1.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
entry2 = tk.Entry(window, width=9, justify="right", font=("Arial", 16))
entry2.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
entry3 = tk.Entry(window, width=9, justify="right", font=("Arial", 16))
entry3.grid(row=2, column=1, columnspan=3, padx=10, pady=10)
entry4 = tk.Entry(window, width=9, justify="right", font=("Arial", 16))
entry4.grid(row=3, column=1, columnspan=3, padx=10, pady=10)
entry5 = tk.Text(window, height=5, width=25, font=("Arial", 16))
entry5.grid(row=4, column=1, columnspan=5, padx=20, pady=20,ipadx=20, ipady=30)

def button_table():
    # 創建表格
    cour = conn.cursor()
    cour.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name = '{}' ''' .format(str(entry1.get())))
    if cour.fetchone()[0] == 1:
        tkinter.messagebox.showerror(title='Done', message="same table name in database")
    else:
        sql = '''Create table '{}'(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                studentID TEXT NOT NULL,
                name TEXT NOT NULL,
                gender TEXT NOT NULL 
            )'''.format(entry1.get())
        cour.execute(sql)
        tkinter.messagebox.showinfo(title='Done', message="table {} create done".format(str(entry1.get())))
    cour.close()

def button_column():#show info
    cour = conn.cursor()
    cour.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name = '{}' ''' .format(str(entry1.get())))
    if cour.fetchone()[0] == 0:
        entry5.delete("1.0", tk.END)
        tkinter.messagebox.showerror(title='Done', message="table {} not found".format(str(entry1.get())))
    else:
        entry5.delete("1.0", tk.END)
        cursor = conn.execute("select * from '{}'".format(str(entry1.get())))
        names = list(map(lambda x: x[0], cursor.description))
        entry5.insert("1.0", str(names))
    cour.close()

def button_value():#search
    cour = conn.cursor()
    sql = f'''select * from "{entry1.get()}" WHERE "{entry2.get()}" = "{entry3.get()}" '''
    result = cour.execute(sql).fetchall()
    entry5.delete("1.0", tk.END)
    for i in result:
        entry5.insert("1.0", str(i)+"\n")
    cour.close()

def button_sql():#submit
    cour = conn.cursor()
    entry5.delete("1.0", tk.END)
    sql=entry4.get()
    result=cour.execute(sql).fetchall()
    conn.commit()
    entry5.insert("1.0", str(result))
    cour.close()

def button_delete():
    cour = conn.cursor()
    cour.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name = '{}' ''' .format(str(entry1.get())))
    if cour.fetchone()[0] == 1:
        cour.execute('''Drop table '{}' ''' .format(entry1.get()))
        cour.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name = '{}' ''' .format(str(entry1.get())))
        if cour.fetchone()[0] == 0:
            tkinter.messagebox.showinfo(title='Done', message="table {} delete done".format(str(entry1.get())))
        else:
            tkinter.messagebox.showerror(title='Done', message="table {} delete error".format(str(entry1.get())))
    else:
        tkinter.messagebox.showerror(title='Done', message="table {} not found".format(str(entry1.get())))
    cour.close()
    
    

button_1 = tk.Button(window, text="create table", height = 2, width = 12, command=lambda: button_table())
button_2 = tk.Button(window, text="show table info", height = 2, width = 12, command=lambda: button_column())
button_3 = tk.Button(window, text="schreach", height = 2, width = 12, command=lambda: button_value())
button_4 = tk.Button(window, text="submit", height = 2, width = 12, command=lambda: button_sql())
button_5 = tk.Button(window, text="del table", height = 2, width = 12, command=lambda: button_delete())

button_1.grid(row=0, column=5)
button_2.grid(row=1, column=5)
button_3.grid(row=2, column=5)
button_4.grid(row=3, column=5)
button_5.grid(row=0, column=10)

window.mainloop()
conn.close()