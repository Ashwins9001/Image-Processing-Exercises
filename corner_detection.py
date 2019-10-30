import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow("Frame")
cv2.createTrackbar("Quality Factor", "Frame", 1, 100, nothing)

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    quality = cv2.getTrackbarPos("Quality Factor", "Frame")
    quality = quality / 100 if quality > 0 else 0.01
    corners = cv2.goodFeaturesToTrack(gray, 100, quality, 20)

    #If no corner, draws non-existing one then error
    if corners is not None:
        corners = np.int0(corners)

        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(frame, (x,y), 3, (0,0,255), -1)
    

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()



#For still image
#img = cv2.imread("squares.jpg")
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#Sum of square differences used around bounding window
#Move window and check where large shifts occur in every dir (corner)
#Maximise SSD for large variation in intensity
#Corner detection based on Shi-Tomasi alteration of Harris detector
#Solve eigenvalues of matrix M such that score R minimal
#corners =  cv2.goodFeaturesToTrack(gray, 10, 0.5, 10)
#corners = np.int0(corners)

#for corner in corners:
#    x, y = corner.ravel()
#    cv2.circle(img, (x,y), 3, (0,0,255), -1)


#cv2.imshow("img", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
