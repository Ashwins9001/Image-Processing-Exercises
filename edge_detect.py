import cv2
import numpy as np

#Demonstration on video
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(frame, (5,5), 0)

    laplacian = cv2.Laplacian(blurred_frame, cv2.CV_64F)
    canny = cv2.Canny(blurred_frame, 50, 150)

    cv2.imshow("Default", frame)
    cv2.imshow("Laplacian", laplacian)
    cv2.imshow("Canny", canny)


    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

#Demonstration on image
#img = cv2.imread("white_panda.jpg", cv2.IMREAD_GRAYSCALE)

#Sobel operator using gradient, apply gaussian to remove noise
#img = cv2.GaussianBlur(img, (5,5), 0)
#sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
#sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)

#Laplacian
#laplacian = cv2.Laplacian(img, cv2.CV_64F)

#Canny
#canny = cv2.Canny(img, 100, 150)


#cv2.imshow("Panda", img)
#cv2.imshow("Sobelx", sobelx)
#cv2.imshow("Sobely", sobely)
#cv2.imshow("Laplacian", laplacian)
#cv2.imshow("Canny", canny)

