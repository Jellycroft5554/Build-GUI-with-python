import tkinter
import math
import tkinter.messagebox


root = tkinter.Tk()
root.geometry("600x500")
root.title("Notes")


def run():

    username_1.get()
    username_1.get()


def run1():


    if username_1.get() == username_12.get() and password_1.get() == password_12.get():

        print("hi " + username_1.get())

        add=tkinter.Button(root, text = "Add Images")
        add.grid(row=4, column=0)

        subtract=tkinter.Button(root, text = "subtract")
        subtract.grid(row=4, column=1)

        resize=tkinter.Button(root, text = "resize")
        resize.grid(row=4, column=2)

    
    else:

        print("ERROR: incorrect credencials " + username_1.get())
        
#signin

sign=tkinter.Label(root, text="sign up")
sign.grid(row=0, column=0, pady=20)


username1=tkinter.Label(root, text="username")
username1.grid(row=1, column=0, pady=20)

username_12=tkinter.Entry(root)
username_12.grid(row=1, column=1, pady=20)


password1=tkinter.Label(root, text="password")
password1.grid(row=2, column=0, pady=20)

password_12=tkinter.Entry(root)
password_12.grid(row=2, column=1, pady=20)


signin=tkinter.Button(root, text="signin", command=run)
signin.grid(row=2, column=2, pady=20)

#login

log=tkinter.Label(root, text="log in")
log.grid(row=0, column=3, pady=20)


username_1=tkinter.Entry(root)
username_1.grid(row=1, column=3, pady=20)


password_1=tkinter.Entry(root)
password_1.grid(row=2, column=3, pady=20)


login=tkinter.Button(root, text="login", command=run1)
login.grid(row=2, column=5, pady=20)


root.mainloop()