import tkinter
import math
import tkinter.messagebox
import random

root = tkinter.Tk()
root.geometry("350x260")
root.title("Guess the Number Game")

number = random.randint(1, 20)

def check_num():
    guess = text_guess.get()
    fuess = int(guess)
    print("Hi")
    if guess > number:
        tkinter.messagebox.showinfo("Too Much","Guess a Smaller Value")
    if guess < number:
        tkinter.messagebox.showinfo("Too Low","Guess a Greater Value")
    if guess == number:
        tkinter.messagebox.showinfo("Good Job","Well Done!!!")

def btn_confirm():
    tkinter.messagebox.showinfo("Welcome", "Well, "+label_name.get()+" I am thinking of a number between 1 to 20")

lable = tkinter.Label(root, text = "Welcome to Our Game")
lable.pack()
label_name=tkinter.Label(root, text="What is Your Name?")
label_name.place(x=10, y=60)
text_name = tkinter.Entry(root)
text_name.place(x=10, y=90)

btnOK = tkinter.Button(root, text="OK", command=btn_confirm)
btnOK.place(x=200, y=90, height=30)

label_guess = tkinter.Label(root, text="Take a Guess")
label_guess.place(x=10, y = 150)
text_guess = tkinter.Entry(root, width=10)
text_guess.place(x=90, y=150)
btnCheck = tkinter.Button(root, text="Guess", command=check_num)
btnCheck.place(x=200, y=150)

root.mainloop()