import cv2
import numpy as np

#video result non-optimal due to image specs, noise
cap = cv2.VideoCapture(0)
template = cv2.imread("polar.jpg", cv2.IMREAD_GRAYSCALE)
width, height = template.shape[::-1] 

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    location = np.where(result >= 0.3)

    for point in zip(*location[::-1]): #np.where returns array row ID, array col ID
        cv2.rectangle(frame, point, (point[0] + width, point[1] + height), (0,255,0), 3)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("template", template)

    key = cv2.waitKey(1)
    
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

#FOR STILL IMAGE
#img = cv2.imread("simpsons.jpg")
#gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#template = cv2.imread("barts_face.jpg", cv2.IMREAD_GRAYSCALE)

#require width/height of template for bounding box
#width, height = template.shape[::-1] #[rows, cols] yet inverted for width, height

#result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
#determine matched image pixel location based on high result metric for match
#equivalent to corner pixel, NOT centroid
#location = np.where(result >= 0.9)

#for points in zip(*location[::-1]): #unpack and pack pixel/coeff into tuple
#    cv2.rectangle(img, points, (points[0]+width, points[1]+height), (0, 255, 0), 3)
    



#cv2.imshow("img", img)
#cv2.imshow("result", result)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
