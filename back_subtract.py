import cv2
import numpy as np
cap = cv2.VideoCapture("highway.mp4")
#Adapts to subtract background with last 120 frames
#Implements gaussian filtering, morpholigcal transforms and shadow detection
#Improves subtraction quality
#Change frame adapation count with history
subtractor = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=25, detectShadows=False)
while True:
    _, frame = cap.read()
    mask = subtractor.apply(frame)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    key = cv2.waitKey(30)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()













#Manual background subtraction
#import cv2
#import numpy as np
#cap = cv2.VideoCapture("highway.mp4")
#_, first_frame = cap.read()
#first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
#first_gray = cv2.GaussianBlur(first_gray, (5,5), 0)
#while True:
#    _, frame = cap.read()
#    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    gray_frame = cv2.GaussianBlur(gray_frame, (5,5), 0)
#    difference = cv2.absdiff(first_gray, gray_frame)
#    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
#    cv2.imshow("Difference", difference)
#    cv2.imshow("Frame", frame)
#    key = cv2.waitKey(30)
#    if key == 27:
#        break
#cap.release()
#cv2.destroyAllWindows()
