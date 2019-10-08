import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

#implement trackbars to fine-tune values for mask 
cv2.namedWindow("Trackbars")

cv2.createTrackbar("L-H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 0, 255, nothing)




while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
 
    
    lower_yellow = np.array([l_h, l_s, l_v])
    upper_yellow = np.array([179, 255, 255]) #according to HSV color space
    #check if array elems of HSV lie between max/min vals
    #whatever is NOT in range comes out as white
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow) 
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", frame)
    cv2.imshow("result", result)
    cv2.imshow("mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
