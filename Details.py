from tkinter import *

window = Tk()
window.geometry("500x500")
window.config(background= "#000000")

Personal=Frame(window, bg="#FFFFFF", width=30)
Personal.pack(padx=20, pady=30)

name=Label(Personal, text="Enter Full Name", width=20,height=2, bg="#FFFFFF",  font=("Comic sans ms",10, "bold"))
name.pack(padx=5, pady=5, side=LEFT)

entername=Entry(Personal,bg="#FFFFFF",  font=("Comic sans ms",10, "bold"))
entername.pack(pady=5, padx=5, side=RIGHT)

Contact=Frame(window, bg="#FFFFFF", width=30)
Contact.pack(padx=20, pady=50)

Number=Label(Contact, text="Enter Phone Number", width=20,height=2, bg="#FFFFFF",  font=("Comic sans ms",10, "bold"))
Number.pack(padx=5, pady=5, side=LEFT)

number=Entry(Contact,bg="#FFFFFF",  font=("Comic sans ms",10, "bold"))
number.pack(pady=5, padx=5, side=RIGHT)

window.mainloop()