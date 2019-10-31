import cv2
import numpy as np

img = cv2.imread("hand.jpg")
#Gaussian pyramid
#Used to downsample images by blurring then reducing size
#Maintains resolution (unless scaled back up)
#Useful for op flow to extend small motion to larger scale w interpolation

layer = img.copy()
gaussian_pyramid = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)

cv2.imshow("0", gaussian_pyramid[0])
cv2.imshow("5", gaussian_pyramid[5])

cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
