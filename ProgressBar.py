from tkinter import *
from tkinter.ttk import *
import time

window=Tk()
window.geometry("400x300")
window.config(bg="black")

def bar_determinate():

    for value in range(0,101,20):
        progress["value"]=value
        window.update_idletasks()
        time.sleep(1)

def bar_indeterminate():

    progress2.start(10)

progress=Progressbar(window, orient=HORIZONTAL, length=280, mode="determinate")
progress.pack(pady=20)

progress2=Progressbar(window, orient=HORIZONTAL, length=280, mode="indeterminate")
progress2.pack(pady=20)

Button1=Button(window, text="determinate", command=bar_determinate).pack(pady=20)

Button2=Button(window, text="indeterminate", command=bar_indeterminate).pack(pady=20)

window.mainloop()