#Image Arithatic Cooperations

import cv2
import numpy as np

#1. Addition

#image1 = cv2.imread("pika.png")
#image2 = cv2.imread("bee.png")
#
#image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
#
#weightedSum = cv2.addWeighted(image1, 0.7, image2, 0.5, 10)
#cv2.imshow("Weighted Image", weightedSum)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#2. Subtraction

#image1 = cv2.imread("pika.png")
#image2 = cv2.imread("bee.png")
#
#image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
#
#subtracted=cv2.subtract(image1, image2)
#cv2.imshow("Substracted Image", subtracted)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#3. Resizing

#image1 = cv2.imread("bee.png")
#
#Resized = cv2.resize(image1, (200, 400))
#
#cv2.imshow("Resized Image", Resized)
#
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#4. Erosion

image = cv2.imread("pika.png", 1)

kernel = np.ones((5, 5), np.uint8)
image = cv2.erode(image, kernel)

cv2.imshow("Eroded image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()