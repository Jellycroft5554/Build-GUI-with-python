from tkinter import *

window = Tk()
window.geometry("490x400")
window.config(background= "#000000")

username = Label(window,text="hello:",font=("comic sans ms", 15, "bold"), bg="grey", fg="blue",height=3, width= 42, anchor="center")
username.place(x=0,y=0)

username = Label(window,text="hola:",font=("comic sans ms", 15, "bold"), bg="blue", fg="black",height=2, width= 20, anchor="center")
username.place(x=0,y=200)


username = Label(window,text="Bojour:",font=("comic sans ms", 15, "bold"), bg="red", fg="green",height=2, width= 21, anchor="center")
username.place(x=250,y=200)

username = Label(window,text="مرحبًا:",font=("comic sans ms", 15, "bold"), bg="red", fg="white",height=2, width= 42, anchor="center")
username.place(x=0,y=330)

username = Label(window,text="你好:",font=("comic sans ms", 15, "bold"), bg="green", fg="gold",height=3, width= 15, anchor="center")
username.place(x=0,y=100)

username = Label(window,text="γεια σου:",font=("comic sans ms", 15, "bold"), bg="beige", fg="maroon",height=3, width= 15, anchor="center")
username.place(x=163.3,y=100)

username = Label(window,text="नमस्ते:",font=("comic sans ms", 15, "bold"), bg="maroon", fg="gold",height=3, width= 15, anchor="center")
username.place(x=326.6,y=100)

username = Label(window,text="مرحبًا:",font=("comic sans ms", 15, "bold"), bg="brown", fg="violet",height=2, width= 42, anchor="center")
username.place(x=0,y=270)

window.mainloop()