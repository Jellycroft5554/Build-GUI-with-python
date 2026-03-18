#Reading and displaying an image using OpenCV
#import cv2
#img = cv2.imread("Pika.png", cv2.IMREAD_ANYCOLOR)
#cv2.imshow("Pikachu Image", img)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()



#read the image and display the images in grey scale
#greyscale is the brightness level
#import cv2
#img = cv2.imread("pika.png",0) # 0 - greyscale
#cv2.imshow("Pikachu in greyscale", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



#sav the resultant greyscale image using opencv and os

#import cv2
#import os
#saved_directory = "C:\\Users\\ryani_jvpdg6k\\OneDrive\\Desktop"

#img = cv2.imread("pika.png", 0)
#cv2.imshow("Pikachu in greyscale", img)
#os.chdir(saved_directory)
#cv2.imwrite("PikaBlackWhite.png", img)
#cv2.waitKey(0)
#print("successfully saved")



#Print an image in different color formats
import cv2
image = cv2.imread("pika.png",1)

#green mode
B, G , R = cv2.split(image)

cv2.imshow("original", image)
cv2.waitKey(0)

cv2.imshow("Blue Saturation", B)
cv2.waitKey(0)

cv2.imshow("Green Saturation", G)
cv2.waitKey(0)

cv2.imshow("Red Saturation", R)
cv2.waitKey(0)

cv2.destroyAllWindows()