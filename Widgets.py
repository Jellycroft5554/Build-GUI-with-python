from tkinter import *

window = Tk()
window.geometry("500x500")
window.config(background= "#fd1540")

#place method

#label

username = Label(window,text="Username:",font=("comic sans ms", 15, "bold"), bg="light blue", fg="dark grey",height=2, width= 20, anchor="center")
username.place(x=150,y=200)

window.mainloop()
