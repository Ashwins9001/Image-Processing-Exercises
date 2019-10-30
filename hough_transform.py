import cv2
import numpy as np

#Lane detection
video = cv2.VideoCapture("road_car_view.mp4")

while True:
    ret, frame = video.read()
    
    #Continue video infinitely when finished
    if not ret:
        video = cv2.VideoCapture("road_car_view.mp4")
        continue
    
    #Yellow lines, apply HSV colorspace range lower -> upper yellow
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_yellow = np.array([18, 94, 140]) #Checked w color selector
    up_yellow = np.array([48, 255, 255])

    #Blur to remove noise 
    blur = cv2.GaussianBlur(hsv,(21,21),0)
    mask = cv2.inRange(hsv, low_yellow, up_yellow)
    
    
    edges = cv2.Canny(mask, 100, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 110, maxLineGap=70)

    #Draw frame-by-frame lines, ensure exist else error 
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv2.line(frame, (x1,y1), (x2,y2), (0,255,0), 3)
        
    
    cv2.imshow("frame", frame)
    cv2.imshow("blur", blur)
    cv2.imshow("mask", edges)

    key = cv2.waitKey(25)

    if key == 27:
        break

video.release()
cv2.destroyAllWindows()

#For still image
#img = cv2.imread("lines.png")
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(gray, 75, 150)

#cv2.imshow("Edges", edges)


#Hough Transform implements accumulator array of custom size
#Array is NxN, stores theta in x, rho in y and any bin equals line
#Determines angles of theta applied to detected edge pixels
#Threshold set to find lines, min num intersecting points
#Probabilistic HT randomly samples edge points to reduce iterations for search/vote
#lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=150)
#print(lines)

#for line in lines:
#    x1, y1, x2, y2 = line[0]
#    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 3)


#cv2.imshow("Image", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
