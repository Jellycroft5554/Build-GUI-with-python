import tkinter
import math
import tkinter.messagebox
import random

root = tkinter.Tk()
root.geometry("600x500")
root.title("Multiplication Table")


entry = tkinter.Entry(root)
entry.grid(column=0, row=0, padx=80, pady=80)


text = tkinter.Label(root, text= "X")
text.grid(column=1, row=0)

entry2 = tkinter.Entry(root)
entry2.grid(column=2, row=0, padx=60, pady=80)



def solve():

    pro = entry.get()
    pro2 = entry2.get()

    product = float(pro)
    product2 = float(pro2)

    answer = product*product2

    formula = product, "*" ,product2, "=" ,answer

    answerbox = tkinter.Label(root, text=formula)
    answerbox.grid(column=2, row=1, columnspan=2)

    
solver= tkinter.Button(root, text="solve",command=solve)
solver.grid(column=0, row=1)

root.mainloop()
