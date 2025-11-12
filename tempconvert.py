from tkinter import *
import tkinter.font as font

my_window = Tk()
my_window.title("Celcius to Fahrenheit")

def convert():
    celecius=float(celcius_value.get())

    fahrenheit=celecius* 9/5 + 32

    output_fahrenheit.config(text=fahrenheit)

#Displaying heading inside window
description = Label(text="Celcius to Fahrenheit", font=font.Font(size=20), fg="grey")
description.pack()

frame = Frame(my_window)
frame.pack(pady=20)

#entry box to enter tempurature in celcius
message_one = Label(frame, text="Please enter valid input...", font=font.Font(size=10))
message_one.grid(row=0, column=0)

celcius_value = Entry(frame)
celcius_value.grid(row=0, column=1)

#To display error Message
error_msg = Label(frame, text="Please enter valid input", font=font.Font(size=8),fg="red")

#Tp display the output
output_fahrenheit = Label(frame, font=font.Font(size=12))
output_fahrenheit.grid(row=2, column=0, columnspan=2, pady=10)

#submit Button
submit_btn = Button(frame, text="convert", width=30, fg="black", bg="lightgreen",
                    padx=20, pady=10, command=convert)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

my_window.geometry("500x250")
my_window.mainloop()