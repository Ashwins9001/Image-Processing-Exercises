import cv2
import numpy as np

video = cv2.VideoCapture("comp_mouse.mp4")

_, first_frame = video.read()
x = 0
y = 30
width = 200
height = 350
roi = first_frame[y: y+ height, x: x + width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#Use first channel, hue (range is 0 - 179)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
#Normalise to fit to 0 - 255 
roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)


#Use this to indicate when to stop iteration (after termination or convergence)
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 3)

while True:
    _, frame = video.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Apply backprojection to determine probability that pixels of following frames
    #Match those of first frame, essentially checking for ROI
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    _, track_window = cv2.meanShift(mask, (x, y, width, height), term_criteria)
    x, y, w, h = track_window
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
    
    cv2.imshow("Mask", mask)
    
    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(60)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()
