from tkinter import *

window = Tk()
window.geometry("500x500")
window.config(background=    "#FFFFFF")

frame=Frame(window, bg="#000000")
frame.pack(padx=20)

label=Label(frame, text="hello", width=20,height=3)
label.pack(pady=20, padx=20, side=RIGHT)

label=Label(frame, text="hey", width=20,height=3)
label.pack(pady=20, padx=20, side=LEFT)

frame2=Frame(window, bg="#FF0000")
frame2.pack(padx=20)

label=Label(frame2, text="hello", width=20,height=3)
label.pack(pady=20, padx=20, side=RIGHT)


window.mainloop()