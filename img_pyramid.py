import cv2
import numpy as np

img = cv2.imread("hand.jpg")

#Gaussian pyramid
#Used to downsample images by blurring then reducing size
#Maintains resolution (unless scaled back up)
#Useful for op flow to extend small motion to larger scale w interpolation
layer = img.copy()
gaussian_pyramid = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)

#Laplacian, applies blur acting as bandpass filter to certain intensity frequencies
#Subtraction b/w original and down-sampled version enhances features
layer = gaussian_pyramid[5]
laplacian_pyramid = [layer]

#reverse iteration (5-0)
for i in range(5, 0, -1): 
    size = (gaussian_pyramid[i-1].shape[1], gaussian_pyramid[i-1].shape[0])
    
    #Start from smallest layer & expand
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
    
    #Size difference can occur if either length/width of down-sampled layer is odd, truncation will result in data loss and size variance when upsampled
    #Compare with prev layer, both should be of equal size
    laplacian = cv2.subtract(gaussian_pyramid[i-1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)
    cv2.imshow(str(i), laplacian)
    


cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
