from tkinter import *
import calendar

window = Tk()
window.geometry("500x500")
window.config(background=    "#0091FF")

def show_calendar():

    cal_new = Tk()
    cal_new.config(background= "light grey")
    cal_new.geometry("800x800")

    year_num = int(year.get())
    cal_content = calendar.calendar(year_num)

    cal_yr=Text(cal_new, padx=30, pady= 20)
    cal_yr.insert(END, cal_content)
    cal_yr.config(state="disabled")
    cal_yr.grid(row=0, column=0, padx=30, pady= 20)

    cal_new.mainloop()

Cal = Label(window, text="Calendar",font=("comic sans ms", 25, "bold"), bg="Grey", fg="Black",height=3, width= 50, anchor="center")
Cal.pack(padx=20, pady=20)

Enter = Label(window, text="Enter Year:",font=("comic sans ms", 15), bg="light green", fg="black",height=1, width= 10, anchor="center")
Enter.pack(padx=20, pady=10)

year = Entry(window, font=("ComicSansms", 25))
year.pack(padx=20, pady=10)

SCalendar=Button(window, text="Show Calendar",font=("comic sans ms", 20),bg="red", fg="black", width=30, command=show_calendar)
SCalendar.pack(padx=20, pady=10)

Exit=Button(window, text="Exit",font=("comic sans ms", 10),bg="red", fg="black", width=30)
Exit.pack(padx=20, pady=20)

window.mainloop()