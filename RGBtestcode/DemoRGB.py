import numpy as np
import cv2 as cv

img = cv.imread('RGB.png')

blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]

cv.imwrite('blue.png', blue)
cv.imwrite('green.png', green)
cv.imwrite('red.png', red)


out = np.zeros(img.shape, dtype="uint8")

out[:, :, 0] = np.zeros([ img.shape[0], img.shape[1]], dtype='uint8')
out[:, :, 1] = green
out[:, :, 2] = red

cv.imwrite("RGwithoutBlue.png", out)
                