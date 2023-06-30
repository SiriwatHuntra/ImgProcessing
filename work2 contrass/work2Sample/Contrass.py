import cv2 as cv
import numpy as np

#op img
img = cv.imread("img.JPG")

#add Intens tran
gramma = 0.1
gramma_corrected = (img/255**gramma)

#scaling ip
gramma_corrected = gramma_corrected*255

#data type convert
img_out = np.array(gramma_corrected, dtype='uint8')

#show img
cv.imshow("PWLaw", img_out)

#save out
cv.imwrite("BE_DIM.png", img)
cv.imwrite("AE_DIM.png", img_out)
