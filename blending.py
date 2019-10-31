import cv2
import numpy as np

img1 = cv2.imread("baseball_ball.png")
img1 = cv2.resize(img1, (1000,1000))
img2 = cv2.imread("football_ball.jpg")
img2 = cv2.resize(img2, (1000,1000))

#Stack image arrays side-by-side along columns
footbaseball_ball = np.hstack((img1[:, :500], img2[:, 500:]))

#Gaussian pyramid 1
layer = img1.copy()
gaussian_pyramid = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)

#Laplacian pyramid 1
layer = gaussian_pyramid[5]
laplacian_pyramid = [layer]
for i in range(5, 0, -1): 
    size = (gaussian_pyramid[i-1].shape[1], gaussian_pyramid[i-1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid[i-1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)

#Gaussian pyramid 2
layer = img2.copy()
gaussian_pyramid2 = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid2.append(layer)

#Laplacian pyramid 2
layer = gaussian_pyramid2[5]
laplacian_pyramid2 = [layer]
for i in range(5, 0, -1): 
    size = (gaussian_pyramid2[i-1].shape[1], gaussian_pyramid2[i-1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid2[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid2[i-1], gaussian_expanded)
    laplacian_pyramid2.append(laplacian)

#Combined Laplacian pyramid from img1 and img2
footbaseball_ball_pyramid = []
#Extract first and second pyramid simultaneously
#Iterate through containers of laplacian pyramid levels
for img1_lap, img2_lap in zip(laplacian_pyramid, laplacian_pyramid2):
    cols, rows, ch = img1_lap.shape
    laplacian = np.hstack((img1_lap[:, 0:int(cols/2)], img2_lap [:, int(cols/2):]))
    footbaseball_ball_pyramid.append(laplacian)

#Reconstruction
footbaseball_ball_reconstructed = footbaseball_ball_pyramid[0]
for i in range(1,6):
    size = (footbaseball_ball_pyramid[i].shape[1], footbaseball_ball_pyramid[i].shape[0])
    #Scaling up from top layer (smallest)
    footbaseball_ball_reconstructed = cv2.pyrUp(footbaseball_ball_reconstructed, dstsize=size)
    footbaseball_ball_reconstructed = cv2.add(footbaseball_ball_pyramid[i], footbaseball_ball_reconstructed)
    
cv2.imshow("Footbase ball reconstructed", footbaseball_ball_reconstructed)
cv2.waitKey(0)
cv2.destroyAllWindows()
