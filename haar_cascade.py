import cv2
import numpy as np
def nothing(x):
    pass
cap = cv2.VideoCapture(0)
#Use adaboost (linear comb weak classifiers) for better efficiency given small size haar feature
#Haar features applied to image, each is calculated subtracting sum of pixels under white rectangle from black
#By applying it to subset of integral image reduces operation to four pixel add/sub
#Use A+D-B-C for corners of rectangle to determine pixel sum of enclosed rectangle 
#Split into seperate rectangles to take haar sum
#Features determine threshold for pos/neg faces
#Apply cascades classifier such that fewer features applied, to discard images obviously not faces
#Continously get screened until numerous features can postively classify, done for efficiency
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cv2.namedWindow("Frame")
cv2.createTrackbar("Scale", "Frame", 11, 20, nothing)
#Use sliding window (kernel) of various sizes for feature detection
#Neighbors only allows face detection if many other windows are nearby
#Higher amount done to eliminate false positives
cv2.createTrackbar("Neighbors", "Frame", 0, 20, nothing)
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    scale = cv2.getTrackbarPos("Scale", "Frame")
    neighbors = cv2.getTrackbarPos("Neighbors", "Frame")
    #Contains rectangle coordinates and width, height containing face
    faces = face_cascade.detectMultiScale(gray, scale/10, 5)
    for rect in faces:
        (x,y,w,h) = rect
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()