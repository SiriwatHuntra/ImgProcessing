import cv2 as cv
import numpy as np

#empty img
img = np.zeros([512, 512], dtype= np.uint8)

#create white squere
for y in range(100, 412):
    for x in range(50, 462):
        img[y,x] = 255

#Display
cv.imshow('Drawing', img)

#Wait for key
cv.waitKey(0)

#clean up
cv.destroyAllWindows()
