import cv2
import numpy as np

img = cv2.imread("red_panda.jpg")
rows, cols, ch = img.shape


scaled_img = cv2.resize(img, None, fx=1/2, fy=1/2)
matrixT = np.float32([[1,0,50], [0,1,50]])
#applies affine transformation -> linear then translation via vector multiplication+addition
#preserve x and y to keep scale given vector sum 
translated_img = cv2.warpAffine(img, matrixT, (cols, rows))
#getRotationMatrix2D(center, degree, scale)
matrixR = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rotated_img = cv2.warpAffine(img, matrixR, (cols, rows))
cv2.imshow("original image", img)
cv2.imshow("scaled image", scaled_img)
cv2.imshow("translated image", translated_img)
cv2.imshow("rotated image", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
