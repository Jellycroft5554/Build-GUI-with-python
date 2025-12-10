import tkinter
import math
import tkinter.messagebox
import random

root = Tk()
root.geometry("500x500")
root.title("Guess The Number")

gnumber=random.randint(1,20)

def check_name():

    print(name2.get())

    p_name=name2.get()

def check_num():

    p_num=number2.get()

Welcome=Label(root, text="Welcome to our game")
Welcome.grid(row=0, column=1, padx=20)

name=Label(root, text="Enter Name")
name.grid(row=1, column=0, padx=20)

name2=Entry(root)
name2.grid(row=1, column=1, padx=20, pady=20)

name3=Button(root, text="Ok")
name3.grid(row=1, column=2, command=check_name())

number=Label(root, text="Enter Number")
number.grid(row=2, column=0, padx=20, pady=20)

number2=Entry(root)
number2.grid(row=2, column=1, padx=20)

number3=Button(root, text="Guess")
number3.grid(row=1, column=2, command=check_num())


root.mainloop()