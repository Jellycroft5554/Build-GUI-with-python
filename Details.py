from tkinter import *

window = Tk()
window.geometry("1200x250")
window.config(background= "#000000")
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.rowconfigure(0,weight=1)

#1

Personal=Frame(window, bg="#FF0000", width=30)
Personal.grid(padx=20, pady=30, column=0, row=0, sticky="nsew")
Personal.columnconfigure(0,weight=1)
Personal.columnconfigure(1,weight=1)
Personal.rowconfigure(0,weight=1)
Personal.rowconfigure(1,weight=1)

name=Label(Personal, text="Enter Full Name", width=20,height=2, bg="#E5B06E",  font=("Comic sans ms",10, "bold"))
name.grid(padx=5, pady=5, column=0, row=0, sticky="nsew")

entername=Entry(Personal,bg="#FF7300",  font=("Comic sans ms",10, "bold"))
entername.grid(pady=5, padx=5, column=0, row=1, sticky="nsew")

Number=Label(Personal, text="Enter Phone Number", width=20,height=2, bg="#FF0000",  font=("Comic sans ms",10, "bold"))
Number.grid(padx=5, pady=5, column=1, row=0, sticky="nsew")

number=Entry(Personal,bg="#26FF00",  font=("Comic sans ms",10, "bold"))
number.grid(pady=5, padx=5, column=1, row=1, sticky="nsew")

#2

Personal2=Frame(window, bg="white", width=30)
Personal2.grid(padx=20, pady=30, column=1, row=0, sticky="nsew")
Personal2.columnconfigure(0,weight=1)
Personal2.columnconfigure(1,weight=1)
Personal2.rowconfigure(0,weight=1)
Personal2.rowconfigure(1,weight=1)

Email=Label(Personal2, text="Enter Email", width=20,height=2, bg="#FF0000",  font=("Comic sans ms",10, "bold"))
Email.grid(padx=5, pady=5, column=0, row=0, sticky="nsew")


enteremail=Entry(Personal2,bg="#00CCFF",  font=("Comic sans ms",10, "bold"))
enteremail.grid(pady=5, padx=5, column=0, row=1, sticky="nsew")

Password=Label(Personal2, text="Enter Password", width=20,height=2, bg="#FF0000",  font=("Comic sans ms",10, "bold"))
Password.grid(padx=5, pady=5, column=1, row=0, sticky="nsew")

Password=Entry(Personal2,bg="#C300FF",  font=("Comic sans ms",10, "bold"))
Password.grid(pady=5, padx=5, column=1, row=1, sticky="nsew")

#3

YOU=Frame(window, bg="#FF0090", width=30)
YOU.grid(padx=20, pady=30, column=2, row=0, sticky="nsew")
YOU.columnconfigure(0,weight=1)
YOU.columnconfigure(1,weight=1)
YOU.rowconfigure(0,weight=1)
YOU.rowconfigure(1,weight=1)

Height=Label(YOU, text="Enter Height", width=20,height=2, bg="#4F1515",  font=("Comic sans ms",10, "bold"))
Height.grid(padx=5, pady=5, column=0, row=0, sticky="nsew")

Height=Entry(YOU,bg="#FFFFFF",  font=("Comic sans ms",10, "bold"))
Height.grid(pady=5, padx=5, column=0, row=1, sticky="nsew")

Weight=Label(YOU, text="Enter Weight", width=20,height=2, bg="#FF0000",  font=("Comic sans ms",10, "bold"))
Weight.grid(padx=5, pady=5, column=1, row=0, sticky="nsew")

Weight=Entry(YOU,bg="#0400FF",  font=("Comic sans ms",10, "bold"))
Weight.grid(pady=5, padx=5, column=1, row=1, sticky="nsew")

window.mainloop()
