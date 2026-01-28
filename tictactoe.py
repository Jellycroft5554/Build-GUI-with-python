import tkinter
import math
import tkinter.messagebox
import random


root = tkinter.Tk()
root.geometry("600x500")
root.title("Multiplication Test")


player1=True
player2=False


#1


#if button1.cget("text")!="X" and button1.cget("text")!="O" or button2.cget("text")!="X" and button2.cget("text")!="O" or button3.cget("text")!="X" and b


def check_x():


    if winnertext.cget("text")!="player1 wins!" and winnertext.cget("text")!="player2 wins!":


        if button1.cget("text")=="X" and button2.cget("text")=="X" and button3.cget("text")=="X":
            winnertext.config(text="player1 wins!")


        elif button4.cget("text")=="X" and button5.cget("text")=="X" and button6.cget("text")=="X":
            winnertext.config(text="player1 wins!")


        elif button7.cget("text")=="X" and button8.cget("text")=="X" and button9.cget("text")=="X":
            winnertext.config(text="player1 wins!")


        elif button1.cget("text")=="X" and button4.cget("text")=="X" and button7.cget("text")=="X":
            winnertext.config(text="player1 wins!")


        elif button2.cget("text")=="X" and button5.cget("text")=="X" and button8.cget("text")=="X":
            winnertext.config(text="player1 wins!")


        elif button3.cget("text")=="X" and button6.cget("text")=="X" and button9.cget("text")=="X":
            winnertext.config(text="player1 wins!")


        elif button1.cget("text")=="X" and button5.cget("text")=="X" and button9.cget("text")=="X":
            winnertext.config(text="player1 wins!")


        elif button7.cget("text")=="X" and button5.cget("text")=="X" and button3.cget("text")=="X":
            winnertext.config(text="player1 wins!")


        else:
            winnertext.config(text="player2 go")
        
def check_o():


    if winnertext.cget("text")!="player1 wins!" and winnertext.cget("text")!="player2 wins!":
        
        if button1.cget("text")=="O" and button2.cget("text")=="O" and button3.cget("text")=="O":
            winnertext.config(text="player2 wins!")


        elif button4.cget("text")=="O" and button5.cget("text")=="O" and button6.cget("text")=="O":
            winnertext.config(text="player2 wins!")


        elif button7.cget("text")=="O" and button8.cget("text")=="O" and button9.cget("text")=="O":
            winnertext.config(text="player2 wins!")


        elif button1.cget("text")=="O" and button4.cget("text")=="O" and button7.cget("text")=="O":
            winnertext.config(text="player2 wins!")


        elif button2.cget("text")=="O" and button5.cget("text")=="O" and button8.cget("text")=="O":
            winnertext.config(text="player2 wins!")


        elif button3.cget("text")=="O" and button6.cget("text")=="O" and button9.cget("text")=="O":
            winnertext.config(text="player2 wins!")


        elif button1.cget("text")=="O" and button5.cget("text")=="O" and button9.cget("text")=="O":
            winnertext.config(text="player2 wins!")


        elif button7.cget("text")=="O" and button5.cget("text")=="O" and button3.cget("text")=="O":
            winnertext.config(text="player2 wins!")




    else:
        winnertext.config(text="player1 go")


winnertext=tkinter.Label(root, text="player1 go")
winnertext.grid(column=2, row=4)


def x_o1():


    if winnertext.cget("text")!="player1 wins!" and winnertext.cget("text")!="player2 wins!" and button1.cget("text")!="X" and button1.cget("text")!="O":
        global player1,player2


        if player1 == True:
            
            button1.config(text="X")
            player1=False
            player2=True
            check_x()


        elif player2 == True:
            button1.config(text="O")
            player1=True
            player2=False
            check_o()


button1=tkinter.Button(root, width=2, command=x_o1)
button1.grid(column=0,row=0, padx=20, pady=20)




def x_o2():
    if winnertext.cget("text")!="player1 wins!" and winnertext.cget("text")!="player2 wins!" and button2.cget("text")!="X" and button2.cget("text")!="O":
        global player1,player2


        if player1 == True:
            button2.config(text="X")
            player1=False
            player2=True
            check_x()


        elif player2 == True:
            button2.config(text="O")
            player1=True
            player2=False
            check_o()




button2=tkinter.Button(root, width=2, command=x_o2)
button2.grid(column=0,row=1, padx=20, pady=20)






def x_o3():
    if winnertext.cget("text")!="player1 wins!" and winnertext.cget("text")!="player2 wins!" and button3.cget("text")!="X" and button3.cget("text")!="O":
        global player1,player2


        if player1 == True:
            button3.config(text="X")
            player1=False
            player2=True
            check_x()


        elif player2 == True:
            button3.config(text="O")
            player1=True
            player2=False
            check_o()






button3=tkinter.Button(root, width=2, command=x_o3)
button3.grid(column=0,row=2, padx=20, pady=20)


#2










def x_o4():
    if winnertext.cget("text")!="player1 wins!" and winnertext.cget("text")!="player2 wins!" and button4.cget("text")!="X" and button4.cget("text")!="O":
        global player1,player2


        if player1 == True:
            button4.config(text="X")
            player1=False
            player2=True
            check_x()


        elif player2 == True:
            button4.config(text="O")
            player1=True
            player2=False
            check_o()


button4=tkinter.Button(root, width=2, command=x_o4)
button4.grid(column=1,row=0, padx=20, pady=20)










def x_o5():
    if winnertext.cget("text")!="player1 wins!" and winnertext.cget("text")!="player2 wins!" and button5.cget("text")!="X" and button5.cget("text")!="O":
        global player1,player2


        if player1 == True:
            button5.config(text="X")
            player1=False
            player2=True
            check_x()


        elif player2 == True:
            button5.config(text="O")
            player1=True
            player2=False
            check_o()


button5=tkinter.Button(root, width=2, command=x_o5)
button5.grid(column=1,row=1, padx=20, pady=20)








def x_o6():
    if winnertext.cget("text")!="player1 wins!" and winnertext.cget("text")!="player2 wins!" and button6.cget("text")!="X" and button6.cget("text")!="O":
        global player1,player2


        if player1 == True:
            button6.config(text="X")
            player1=False
            player2=True
            check_x()


        elif player2 == True:
            button6.config(text="O")
            player1=True
            player2=False
            check_o()


button6=tkinter.Button(root, width=2, command=x_o6)
button6.grid(column=1,row=2, padx=20, pady=20)


#3








def x_o7():
    if winnertext.cget("text")!="player1 wins!" and winnertext.cget("text")!="player2 wins!" and button7.cget("text")!="X" and button7.cget("text")!="O":
        global player1,player2


        if player1 == True:
            button7.config(text="X")
            player1=False
            player2=True
            check_x()


        elif player2 == True:
            button7.config(text="O")
            player1=True
            player2=False
            check_o()


button7=tkinter.Button(root, width=2, command=x_o7)
button7.grid(column=2,row=0, padx=20, pady=20)








def x_o8():
    if winnertext.cget("text")!="player1 wins!" and winnertext.cget("text")!="player2 wins!" and button8.cget("text")!="X" and button8.cget("text")!="O":
        global player1,player2


        if player1 == True:
            button8.config(text="X")
            player1=False
            player2=True
            check_x()


        elif player2 == True:
            button8.config(text="O")
            player1=True
            player2=False
            check_o()






button8=tkinter.Button(root, width=2, command=x_o8)
button8.grid(column=2,row=1, padx=20, pady=20)






def x_o9():
    if winnertext.cget("text")!="player1 wins!" and winnertext.cget("text")!="player2 wins!" and button9.cget("text")!="X" and button9.cget("text")!="O":
        global player1,player2


        if player1 == True:
            button9.config(text="X")
            player1=False
            player2=True
            check_x()


        elif player2 == True:
            button9.config(text="O")
            player1=True
            player2=False
            check_o()






button9=tkinter.Button(root, width=2, command=x_o9)
button9.grid(column=2,row=2, padx=20, pady=20)


root.mainloop()
