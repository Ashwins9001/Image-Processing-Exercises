import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("sea_beach.jpg")
b, g, r = cv2.split(img)
cv2.imshow("b", b)
cv2.imshow("r", r)
cv2.imshow("g", g)

#ravel flattens intensity values to 1D array
#hist(array, BIN, range) - BIN is # pixels used to rep hist
#provide distribution of intensity vals
#for RGB can split by color, hist each channel
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])

plt.show()
