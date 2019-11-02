import cv2
import numpy as np
from matplotlib import pyplot as plt
original_image = cv2.imread("goalkeeper.jpg")
roi = cv2.imread("pitch_ground.jpg")
hsv_original = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(hsv_roi)


#Histogram ROI
roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0,180, 0,256])
mask = cv2.calcBackProject([hsv_original], [0,1], roi_hist, [0, 180, 0, 256], 1)
#Remove noise via filter
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
mask = cv2.filter2D(mask, -1, kernel)
_, mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
#Merge three channels of mask to apply grayscale for bitwise op
mask = cv2.merge((mask, mask, mask))
#Pick mask out from original
result = cv2.bitwise_and(original_image, mask)

cv2.imshow("Original image", original_image)
cv2.imshow("mask", mask)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
