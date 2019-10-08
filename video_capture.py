import cv2
import numpy as np

cap = cv2.VideoCapture("red_panda_snow.mp4")

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("red_panda.avi", fourcc, 25, (640, 360))



while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    out.write(frame)
    key = cv2.waitKey(60)
    if key == 27:
        break

out.release()
cap.release()
cv2.destroyAllWindows()
