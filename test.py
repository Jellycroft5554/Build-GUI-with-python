import tkinter
import math
import tkinter.messagebox
import random

root = tkinter.Tk()
root.geometry("600x500")
root.title("Multiplication Test")

pro=random.randint(0,12)

pro2=random.randint(0,12)

entry = tkinter.Label(root, text=pro)
entry.grid(column=0, row=0, padx=40, pady=80)

text = tkinter.Label(root, text= "X")
text.grid(column=1, row=0, padx=40)

entry2 = tkinter.Label(root, text=pro2)
entry2.grid(column=2, row=0, padx=40, pady=80)

text2 = tkinter.Label(root, text= "=")
text2.grid(column=3, row=0, padx=40)

answerbox = tkinter.Entry(root)
answerbox.grid(column=4, row=0)

result = tkinter.Label(root, text="check carefully")
result.grid(column=1, row=1, padx=40)


def check():

    ans = answerbox.get()
    answer = int(ans)

    if answer == pro * pro2:

        result.config(text="well done")

    else:
        result.config(text="try again")
    
checker = tkinter.Button(root, text="check", command=check)
checker.grid(column=0, row=1)

root.mainloop()