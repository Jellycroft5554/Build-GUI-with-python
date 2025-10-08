import tkinter as tk
from tkinter.ttk import *
import time

root = tk.Tk()
root.configure(bg="#e16161")
root.geometry("1500x1400")

def number_only(char):
    return char.isdigit() or char==""

tk.Label(root, text="Hello, would you like to place an order or pick up?", bg="#e16161", fg="white", width=42, font=("Comic sans ms",20, "bold")).grid(row=0, column=0, padx=5, pady=42)
order_pick = tk.Entry(root, font=("Comic sans ms",20, "bold"))
order_pick.grid(row=0, column=1, padx=5, pady=42)

tk.Label(root, text="Name the order is under;", bg="#e16161", fg="white", width=30, font=("Comic sans ms",20, "bold")).grid(row=1, column=0, padx=5, pady=42)
Name_order = tk.Entry(root, font=("Comic sans ms",20, "bold"))
Name_order.grid(row=1, column=1, padx=5, pady=42)

tk.Label(root, text="What meal would you like?", 
         bg="#e16161", fg="white", font=("Comic sans ms",20, "bold")).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

food_frame = tk.Frame(root, bg="#e16161", width=30)
food_frame.grid(row=3, column=0, columnspan=2, padx=100, pady=20)

food_scroll = tk.Spinbox(food_frame,from_=1,to=10, width=30, state="readonly", font=("Comic sans ms",30, "bold"))
food_scroll.pack(side=tk.RIGHT, fill=tk.Y, padx=20)

food_list = ["Hamburger", "Cheeseburger", "Salad Bowl","Chicken Nuggets", "None"]
food_spin = tk.Spinbox(food_frame, value=food_list, state="readonly", font=("Comic sans ms",30, "bold"))
food_spin.pack()

tk.Label(root, text="What beverage would you like?", 
         bg="#e16161", fg="white", font=("Comic sans ms",20, "bold")).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

bev_frame = tk.Frame(root, bg="#e16161", width=30)
bev_frame.grid(row=6, column=0, columnspan=2, padx=100, pady=20)

bev_scroll = tk.Spinbox(bev_frame,from_=1,to=10, width=30, state="readonly", font=("Comic sans ms",30, "bold"))
bev_scroll.pack(side=tk.RIGHT, fill=tk.Y, padx=20)

bev_list = ["Pepsi", "Sprite", "Orange Juice", "Apple Juice", "Water", "None"]
bev_spin = tk.Spinbox(bev_frame, value=bev_list, state="readonly", font=("Comic sans ms",30, "bold"))
bev_spin.pack()

tk.Label(root, text="What side would you like?", 
         bg="#e16161", fg="white", font=("Comic sans ms",20, "bold")).grid(row=7, column=0, columnspan=2, padx=5, pady=5)

side_frame = tk.Frame(root, bg="#e16161", width=30)
side_frame.grid(row=8, column=0, columnspan=2, padx=100, pady=20)

side_scroll = tk.Spinbox(side_frame,from_=1,to=10, width=30, state="readonly", font=("Comic sans ms",30, "bold"))
side_scroll.pack(side=tk.RIGHT, fill=tk.Y, padx=20)

side_list = ["French Fries", "Starter Salad", "Bread", "Coleslaw", "None"]
side_spin = tk.Spinbox(side_frame, value=side_list, state="readonly", font=("Comic sans ms",30, "bold"))
side_spin.pack()

tk.Label(root, text="What dessert would you like?", 
         bg="#e16161", fg="white", font=("Comic sans ms",20, "bold")).grid(row=9, column=0, columnspan=2, padx=5, pady=5)

des_frame = tk.Frame(root, bg="#e16161", width=30)
des_frame.grid(row=10, column=0, columnspan=2, padx=100, pady=20)

des_scroll = tk.Spinbox(des_frame,from_=1,to=10, width=30, state="readonly", font=("Comic sans ms",30, "bold"))
des_scroll.pack(side=tk.RIGHT, fill=tk.Y, padx=20)

des_list = ["Vanilla Ice Cream", "Chocolate Ice Cream", "Jelly", "Chocolate Cake", "None"]
des_spin = tk.Spinbox(des_frame, value=des_list, state="readonly", font=("Comic sans ms",30, "bold"))
des_spin.pack()

tk.Label(root, text="Card number", bg="#e16161", fg="white", width=10, font=("Comic sans ms",20, "bold")).grid(row=11, column=0, padx=20, pady=20)
Card = tk.Entry(root, font=("Comic sans ms",20, "bold"))
Card.grid(row=11, column=1, padx=20, pady=20)

tk.Label(root, text="CVV", bg="#e16161", fg="white", width=10, font=("Comic sans ms",20, "bold")).grid(row=12, column=0, padx=20, pady=20)
CVV = Entry(root, font=("Comic sans ms",20, "bold"), validatecommand=(root.register(number_only),"%P"))
CVV.grid(row=12, column=1, padx=20, pady=20)

tk.Label(root, text="Exp", bg="#e16161", fg="white", width=10, font=("Comic sans ms",20, "bold")).grid(row=13, column=0, padx=20, pady=20)
Exp = tk.Entry(root, font=("Comic sans ms",20, "bold"))
Exp.grid(row=13, column=1, padx=20, pady=20)

tk.Label(root, text="Pin", bg="#e16161", fg="white", width=10, font=("Comic sans ms",20, "bold")).grid(row=14, column=0, padx=20, pady=20)
Pin = tk.Entry(root, font=("Comic sans ms",20, "bold"), show="*")
Pin.grid(row=14, column=1, padx=20, pady=20)

def bar_determinate():

    for value in range(0,101,20):
        progress["value"]=value
        root.update_idletasks()
        time.sleep(3)

    root.destroy()

progress = Progressbar(root, orient="horizontal", length=560, mode="determinate")
progress.grid(row=15, column=0,pady=20)

Confirm = tk.Button(root, text="Confirm Order", width=30, font=("Comic sans ms",30, "bold"), command= bar_determinate)
Confirm.grid(row=16, column=0, columnspan=2, pady=20)


root.mainloop()