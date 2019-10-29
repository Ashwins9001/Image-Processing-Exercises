import cv2
import numpy as np

img = cv2.imread("book_page.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mean_c = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 12)
gauss = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 12)


cv2.imshow("mean_c", mean_c)
cv2.imshow("gauss", gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()
