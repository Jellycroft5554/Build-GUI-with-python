from tkinter import *

window = Tk()
window.geometry("750x750")
window.config(background="grey")

def convert():

    error_message=Label(window, text="please enter valid input")

    C_F = box.get()
    
    if (C_F.replace(".", "", 1).isdigit()):

        error_message.grid_forget()

        tempf=(float(C_F) * 9 / 5)+32

        labelF.config(text="Temp in °F:" + str(tempf))

    else:

        error_message.grid(row=1, column=1)


label=Label(window, text="Celcius->Fahrenheit",font=("Comic sans ms",20, "bold"), width=40, height=3, bg="light grey")
label.grid(row=0, column=0, columnspan=3, pady=20)

label2=Label(window, text="Enter Temp in °C:", width=20 ,height=3, font=("Comic sans ms",10, "bold"), bg="light grey")
label2.grid(row=1, column=0, pady=20)

box=Entry(window, font=("Comic sans ms",10, "bold"))
box.grid(row=1, column=2, pady=20)

labelF=Label(window, width=20, height=3, text="Temp in °F:", font=("Comic sans ms",10, "bold"), bg="light grey")
labelF.grid(row=2, column=1, pady=20)

submit_button = Button(window, text="Convert", width=10, font=("Comic sans ms",20, "bold"), command=convert())
submit_button.grid(row=3, column=1, pady=20)

window.mainloop()