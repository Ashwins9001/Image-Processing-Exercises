import cv2
import numpy as np

#Control when point2 function begins to run
drawing = False

#Define top-left, bottom-right points rect
point1 = ()
point2 = ()

def mouse_drawing(event, x, y, flags, params):
    global point1, point2, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        #Append click as pos to display
        #circles.append((x,y))
        if drawing is False:
            drawing = True
            point1 = (x,y)
        else:
            #Freeze rectangle drawing after depressing lmbt
            drawing = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            point2 = (x,y)

cap = cv2.VideoCapture(0)
cv2.namedWindow("Frame")
#mouse_drawing no params, setMouseCallback will call it on event proper input 
cv2.setMouseCallback("Frame", mouse_drawing)

#Store positions in variable to prevent disappearance on frame refresh
#circles = []

while True:
    _, frame = cap.read()

    #Iterate through circles array constantly 
    #for center_pos in circles:
        #cv2.circle(frame, center_pos, 5, (0,0,255), -1)

    if point1 and point2:
        cv2.rectangle(frame, point1, point2, (0,0,255))
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
