import numpy as np
import cv2 as cv

#empty img
img = np.zeros([300, 300], dtype= np.uint8)

#get input
# h,k is x,y of circle center
Radius = 80
RadiusLine = 5
h = 150
k = 150

#draw a circle
for x in range(img.shape[1]):
    for y in range(img.shape[0]):
        if ((x - h) ** 2) + ((y - k) ** 2) in range(Radius, Radius + RadiusLine):
             img[y, x] = 255

#Display
cv.imshow('Drawing', img)

#Wait for key
cv.waitKey(0)

#clean up
cv.destroyAllWindows()
