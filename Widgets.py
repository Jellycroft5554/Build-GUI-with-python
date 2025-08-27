from tkinter import *

window = Tk()
window.geometry("1000x800")
window.config(background= "#000000")

#Place method

"""

#label

username = Label(window,text="Username:",font=("comic sans ms", 15, "bold"), bg="light blue", fg="dark grey",height=2, width= 20, anchor="center")
username.place(x=30,y=200)

#Entry box

uname = Entry(window, font=("ComicSansms", 40))
uname.place(x=400,y=200)

password = Label(window,text="Password:",font=("comic sans ms", 15, "bold"), bg="light blue", fg="dark grey",height=2, width= 20, anchor="center")
password.place(x=30,y=400)

pname = Entry(window, font=("ComicSansms", 40))
pname.place(x=400,y=400)

#Button

submit=Button(window, text="Submit:",font=("comic sans ms", 15, "bold"), width=30)
submit.place(x=370,y=600)

"""

"""

#Pack Method-Vertical

username = Label(window, text="Username:",font=("comic sans ms", 15, "bold"), bg="light blue", fg="dark grey",height=2, width= 20, anchor="center")
username.pack(padx=20, pady=40)

uname = Entry(window, font=("ComicSansms", 40))
uname.pack(padx=20, pady=40)

password = Label(window, text="Password:",font=("comic sans ms", 15, "bold"), bg="light blue", fg="dark grey",height=2, width= 20, anchor="center")
password.pack(padx=20, pady=40)

pname = Entry(window, font=("ComicSansms", 40))
pname.pack(padx=20, pady=40)

submit=Button(window, text="Submit:",font=("comic sans ms", 15, "bold"), width=30)
submit.pack(padx=20, pady=40)
"""

"""
#Pack Method-Horisontal

username = Label(window, text="Username:",font=("comic sans ms", 15, "bold"), bg="light blue", fg="dark grey",height=2, width= 20, anchor="center")
username.pack(padx=20, pady=40, side=LEFT)

uname = Entry(window, font=("ComicSansms", 40))
uname.pack(padx=20, pady=40, side=LEFT)

password = Label(window, text="Password:",font=("comic sans ms", 15, "bold"), bg="light blue", fg="dark grey",height=2, width= 20, anchor="center")
password.pack(padx=20, pady=40, side=LEFT)

pname = Entry(window, font=("ComicSansms", 40))
pname.pack(padx=20, pady=40, side=LEFT)

submit=Button(window, text="Submit:",font=("comic sans ms", 15, "bold"), width=30)
submit.pack(padx=20, pady=40, side=LEFT)
"""

#Grid Method-Rows and Columns

username = Label(window, text="Username:",font=("comic sans ms", 15, "bold"), bg="light blue", fg="dark grey",height=2, width= 20, anchor="center")
username.grid(row=0, column=0, pady=20)

uname = Entry(window, font=("ComicSansms", 40))
uname.grid(row=0, column=1, pady=20)

password = Label(window, text="Password:",font=("comic sans ms", 15, "bold"), bg="light blue", fg="dark grey",height=2, width= 20, anchor="center")
password.grid(row=1, column=0, pady=20)

pname = Entry(window, font=("ComicSansms", 40))
pname.grid(row=1, column=1, pady=20)

submit=Button(window, text="Submit:",font=("comic sans ms", 15, "bold"), width=30)
submit.grid(row=2, column=0, columnspan=2, pady=20)

window.mainloop()