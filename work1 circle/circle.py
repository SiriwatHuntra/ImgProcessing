import numpy as np
import cv2 as cv

#empty img
img = np.zeros([512, 512], dtype= np.uint8)

#get input
# h,k is x,y of circle center
Radius = 80
h = 256
k = 256

#draw a circle
for x in range(img.shape[1]):
    for y in range(img.shape[0]):
        if ((x - h) ** 2) + ((y - k) ** 2) <= Radius ** 2 :
             img[y, x] = 255

#Display
cv.imshow('Drawing', img)

#Wait for key
cv.waitKey(0)

#clean up
cv.destroyAllWindows()
