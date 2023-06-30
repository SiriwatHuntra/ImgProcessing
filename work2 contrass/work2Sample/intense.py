import cv2 as cv
import numpy as np

img = cv.imread('dim.png')

img_out = np.log(img)

img_max = np.max(img_out)
img_out = img_out*(255/img_max)

img_out = np.array(img_out, dtype=np.uint8)

cv.imwrite("DemoIntenst.png", img_out)
