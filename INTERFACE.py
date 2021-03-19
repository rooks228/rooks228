import tkinter
import tkinter as tk
from tkinter import *
click = 6
app = tk.Tk()
app.geometry("400x360")
app.title("My_GUI_ToDo")
app['bg'] = "#7B68EE"


def create_Label():
    global click
    click += 1
    print(click)



frame1 = Frame(bg = "#008B8B")

frame1.pack(fill=X)

lbl1 = Label(frame1, text="Задача", width=10)
lbl1.pack(side=LEFT, padx=9, pady=5)

entry1 = Entry(frame1)
entry1.pack(fill=X, padx=9, expand=True)

frame2 = Frame(bg = "#008B8B")
frame2.pack(fill=X)

lbl2 = Label(frame2, text="Номер", width=10)
lbl2.pack(side=LEFT, padx=9, pady=5)

entry2 = Entry(frame2)
entry2.pack(fill=X, padx=9, expand=True)

btn = Button(frame2,text = "Записать")
btn.pack(fill=BOTH, pady=5, padx=9)

frame3 = Frame(bg="#BC8F8F")
frame3.pack(fill=BOTH, expand=True)

lbl3 = Label(frame3, text="Задачи", width=10)
lbl3.pack(side=LEFT, anchor=N, padx=9, pady=30)

txt = Text(frame3, height = 15)
txt.pack(fill=BOTH, pady=5, padx=9, expand=0)






app.mainloop()
