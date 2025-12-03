from tkinter import *
from tkinter.ttk import *
from time import strftime
import random

root = Tk()
root.title("Clock")

colours=["red", "orange", "yellow", "green", "blue", "pink", "purple"]

def time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text=string, background=random.choice(colours), foreground=random.choice(colours))
    lbl.after(1000, time)




lbl = Label(root, font=("calibri",40,"bold"), background="orange", foreground="white")
lbl.pack(anchor="center")

time()
mainloop()