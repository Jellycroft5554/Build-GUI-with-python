from tkinter import *

window = Tk()
window.geometry("500x320")
window.config(background=    "#FFFFFF")

Calendar = Label(window, text="Calendar",font=("comic sans ms", 25, "bold"), bg="Grey", fg="Black",height=3, width= 50, anchor="center")
Calendar.pack(padx=20, pady=0)

Enter = Label(window, text="Enter Year:",font=("comic sans ms", 15), bg="light green", fg="black",height=1, width= 10, anchor="center")
Enter.pack(padx=20, pady=0)

year = Entry(window, font=("ComicSansms", 25))
year.pack(padx=20, pady=0)

SCalendar=Button(window, text="Show Calendar",font=("comic sans ms", 20),bg="red", fg="black", width=30)
SCalendar.pack(padx=20, pady=0)

Exit=Button(window, text="Exit",font=("comic sans ms", 10),bg="red", fg="black", width=30)
Exit.pack(padx=20, pady=0)

window.mainloop()