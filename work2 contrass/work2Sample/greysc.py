import numpy as np
import cv2 as cv

img = cv.imread('img.JPG', cv.IMREAD_GRAYSCALE)

img_out = cv.equalizeHist(img)

cv.imwrite('BEfore.png', img)
cv.imwrite('AFter.png', img_out)
