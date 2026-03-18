import cv2
import numpy as np
from tkinter import *
import tkinter
import math
import tkinter.messagebox


root = Tk()
root.title("Image Buttons")
root.geometry("300x200")


img1 = cv2.imread("pika.png")
img2 = cv2.imread("bee.png")


img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))




def resize_image():
    img1 = cv2.imread("bee.png")
    Resized = cv2.resize(img1, (200, 400))
    cv2.imshow("Resized Image", Resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def add_images():
    added = cv2.add(img1, img2)
    cv2.imshow("Added Image", added)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def subtract_images():
    subtracted = cv2.subtract(img1, img2)
    cv2.imshow("Subtracted Image", subtracted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


Resize=Button(root, text="Resize", command=resize_image)
Resize.pack(pady=10)


Add=Button(root, text="Add", command=add_images)
Add.pack(pady=10)


Sub=Button(root, text="Subtract", command=subtract_images) 
Sub.pack(pady=10)


root.mainloop()
