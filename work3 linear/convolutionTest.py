import cv2 as cv
import numpy as np

img = cv.imread("gimg.jpeg")
Ikernel = cv.imread("line.jpeg")

n = Ikernel.sum()
Ikernel = Ikernel/n

img = cv.filter2D(src = img, ddepth=1, kernel=Ikernel)

cv.imwrite('Conv.jpeg', img)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
