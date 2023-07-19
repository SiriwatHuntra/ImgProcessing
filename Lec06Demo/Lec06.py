import numpy as np
import cv2 as cv

img = cv.imread("Cat.png", cv.IMREAD_img_graySCALE)

#set data 2 32bits 
img = img.astype(np.float32)

#take fourier transform
imgF = np.fft.fft2(img)

#shift 0,0 to center of img
imgF = np.fft.fftshift(imgF)

# find magnitude & phase
imgReal = np.real(imgF)
imgLma = np.imag(imgF)
imgMag = np.sqrt(imgReal**2 + imgLma**2)
imgPhs = np.arctan2(imgLma, imgReal)

#inverse fourier trans
imgRealInv = imgMag*np.cos(imgPhs)
imgLmaInv = imgMag*np.sin(imgPhs)

imgFInv = imgRealInv + imgLmaInv*1j

imgFInv = np.fft.fftshift(imgFInv)
imgInv = np.fft.fft2(imgFInv)

imgInv = np.real(imgInv) 
imgInv = imgInv.astype(np.uint8)

cv.imwrite("input.png", img)
cv.imwrite("output.png", imgInv)

#display
imgMag = np.log(1+imgMag)
imgMag = cv.normalize(imgMag, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
cv.imwrite("magnitude.png", imgMag)

#Out put check
print("Success")