import cv2
import numpy as np

img = cv2.imread("the_book_thief.jpg", cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create(nfeatures=1500)
keypoints, descriptors = orb.detectAndCompute(img,None)
img = cv2.drawKeypoints(img, keypoints, None)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
