import cv2 as cv 
import numpy as np

def sobel_fil(img_gray):
        
    # Define Sobel kernels
    sobel_x = np.array([
        [1, 0, -1], 
        [2, 0, -2], 
        [1, 0, -1]])
    
    sobel_y = np.array([
        [1, 2, 1], 
        [0, 0, 0], 
        [-1, -2, -1]])
        
    # Apply Sobel kernels to the image
    grad_x = cv.filter2D(img_gray, -1, sobel_x)

    # Calculate the magnitude of the gradients
    grad = np.sqrt(grad_x**2)
        
    # Normalize the gradient values to the range [0, 255]
    grad = grad.astype(np.uint8)
    grad = cv.normalize(grad, None, 0, 255, cv.NORM_MINMAX)

    cv.imwrite("Sobel_out.png", grad_x)
    return cv.imread("Sobel_out.png")

def Frequency_D(img):
    img = np.fft.fft2(img)
    img = np.fft.fftshift(img)
    img = np.abs(img)
    magnitude = 16 * np.log(np.abs(img))
    return magnitude
    
def DotbyDot(img1, img2):
    inF = img1
    SobelF = img2
    DotByDot = np.multiply(inF, SobelF)
    DbD_img = np.fft.fftshift(DotByDot)
    DbD_img = np.fft.fft2(DotByDot)
    DbD_img = np.abs(DbD_img)
    DbD_img = cv.normalize(DbD_img, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    cv.imwrite('DbD_result.png', DotByDot)
    return DbD_img

def Freq_to_spatial(img):
    spatial = np.fft.fft2(np.fft.fftshift(img))
    spatial = np.abs(spatial)
    spatial = cv.normalize(spatial, None, 0, 255, cv.NORM_MINMAX, dtype=cv.CV_8U)
    cv.imwrite('Spatial.png', spatial)




img = cv.imread("Cat.png", cv.IMREAD_GRAYSCALE)
img = cv.Sobel(img, cv.CV_64F, 1, 0, ksize = 3)
#sobel_fil(img)
cv.imwrite("Sobel_out.png", img)


inF = cv.imread("Cat.png", cv.IMREAD_GRAYSCALE)
SobelF = cv.imread("Sobel_out.png", cv.IMREAD_GRAYSCALE)

cv.imwrite("In_F.png", Frequency_D(inF))
cv.imwrite("Sobel_F.png", Frequency_D(SobelF))

inF = cv.imread("Cat.png", cv.IMREAD_GRAYSCALE)
SobelF = cv.imread("Sobel_out.png", cv.IMREAD_GRAYSCALE)
DdD_img = DotbyDot(inF, SobelF)

img_dbd = cv.imread("Sobel_F.png", cv.IMREAD_GRAYSCALE)
Freq_to_spatial(DdD_img)

#code check
print("Success!")
