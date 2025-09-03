from tkinter import *

window=Tk()
window.geometry("1000x1000")
window.config(bg="grey")

scroll_bar=Scrollbar(window)
scroll_bar.pack(side=RIGHT,fill=Y)

list_box=Listbox(window, height=10, width=20, bg="light blue", activestyle="dotbox", font=("ComicSansms", 40 ),yscrollcommand=scroll_bar.set)

colours=Label(window, height=2, width=20, text="colours", font=("ComicSansms", 20 ))
colours.pack(side=LEFT, padx=30, pady=30)

list_box.pack(side=LEFT, fill=BOTH, padx=30, pady=20)

scroll_bar.config(command=list_box.yview)

list_box.insert(1,"red")
list_box.insert(2,"red")
list_box.insert(3,"red")
list_box.insert(4,"rfed")
list_box.insert(5,"refd")
list_box.insert(6,"red")
list_box.insert(7,"refd")
list_box.insert(8,"red")
list_box.insert(9,"red")
list_box.insert(10,"red")
list_box.insert(11,"resd")
list_box.insert(12,"red")
list_box.insert(13,"resd")
list_box.insert(14,"red")
list_box.insert(15,"red")
list_box.insert(16,"red")
list_box.insert(17,"red")
list_box.insert(18,"red") 

window.mainloop()