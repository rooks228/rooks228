import tkinter
import tkinter as tk
from tkinter import *
import  _sqlite3 as sql
import tkinter.ttk as ttk
click = 0
app = tk.Tk()
app.geometry("400x360")
app.title("My_GUI_ToDo")
app['bg'] = "#7B68EE"
con = sql.connect("DB.bd")






with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `user` (`click` INTEGER, `task` STREING, `stock` INTEGER)")




def writ():
    cur.execute("SELECT * FROM `user`")
    rows = cur.fetchall()
    global click
    value = ERROR()
    if (value == 0):
        return
    click += 1
    for row in rows:

        txt.insert('1.0', str(click) + " --> " + str(row) + "\n")



def delete():
    y = float(entry1.get())
    cur.execute("DELETE FROM `user` WHERE click = ?",(y,))


def redact():
    y = float(entry1.get())
    H = str(entry9.get())
    cur.execute("UPDATE `user` SET task = ? WHERE click = ?",(H,y,))





def create_Label():
    global click
    value = ERROR()
    if(value == 0):
        return
    click += 1
    var = entry1.get()
    cur.execute(f"INSERT INTO `user` VALUES ('{click}','{var}', '{click}')")
    writ()



def ERROR():
    dsf = str("ERROR")
    if entry1.get() == "":
        txt.insert('1.0', dsf +' here is my text to insert'+"\n")




frame1 = Frame(bg = "#008B8B")

frame1.pack(fill=X)

lbl1 = Label(frame1, text="Задача", width=10)
lbl1.pack(side=LEFT, padx=9, pady=5)


entry1 = Entry(frame1)
entry1.pack(fill=X, padx=9, expand=True)

entry9 = Entry(frame1)
entry9.pack(fill=X, padx=9, expand=True)

frame2 = Frame(bg = "#008B8B")
frame2.pack(fill=X)

lbl2 = Label(frame2, text="Номер", width=10)
lbl2.pack(side=LEFT, padx=9, pady=5)



btn = Button(frame2,text = "Записать", command = create_Label)
btn.pack(fill=BOTH, pady=5, padx=9)

btn = Button(frame2,text = "показать", command = writ)
btn.pack(fill=BOTH, pady=5, padx=9)

btn = Button(frame2,text = "удалить", command = delete)
btn.pack(fill=BOTH, pady=5, padx=9)

btn = Button(frame2,text = "redact", command = redact)
btn.pack(fill=BOTH, pady=5, padx=9)

frame3 = Frame(bg="#BC8F8F")
frame3.pack(fill=BOTH, expand=True)

lbl3 = Label(frame3, text="Задачи", width=10)
lbl3.pack(side=LEFT, anchor=N, padx=9, pady=30)

txt = Text(frame3, height = 15)
txt.pack(fill=BOTH, pady=5, padx=9, expand=0)






app.mainloop()
con.commit()
cur.close()
