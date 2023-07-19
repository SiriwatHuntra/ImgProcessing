import cv2 as cv 
import numpy as np

def sobel_fil(img_gray):
    # Convert image to img_grayscale
        
    # Define Sobel kernels
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        
    # Apply Sobel kernels to the image
    grad_x = cv.filter2D(img_gray, -1, sobel_x)
    grad_y = cv.filter2D(img_gray, -1, sobel_y)
        
    # Calculate the magnitude of the gradients
    grad = np.sqrt(grad_x**2 + grad_y**2)
        
    # Normalize the gradient values to the range [0, 255]
    grad = grad.astype(np.uint8)
    grad = cv.normalize(grad, None, 0, 255, cv.NORM_MINMAX)

    cv.imwrite("Sobel_out.png", grad)
    return cv.imread("Sobel_out.png")

def Frequency_D(img):
    img = np.fft.fft2(img)
    img = np.fft.fftshift(img)
    img = np.abs(img)
    magnitude = 16 * np.log(img)
    return magnitude
    

    
img = cv.imread("Cat.png", cv.IMREAD_GRAYSCALE)
sobel_fil(img)

inF = cv.imread("Cat.png", cv.IMREAD_GRAYSCALE)
cv.imwrite("In_F.png", Frequency_D(inF))

SobelF = cv.imread("Sobel_out.png", cv.IMREAD_GRAYSCALE)
cv.imwrite("Sobel_F.png", Frequency_D(SobelF))

DotByDot = np.multiply(inF, SobelF)
DbD_img = np.fft.ifftshift(DotByDot)
DbD_img = np.fft.ifft2(DbD_img)
DbD_img = np.abs(DbD_img)
DbD_img = cv.normalize(DbD_img, None, 0, 255, cv.NORM_MINMAX, dtype=cv.CV_8U)
cv.imwrite('DbD_result.png', DbD_img)


#code check
print("Success!")
