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

    cv.imwrite("OutPut.png", grad)

img = cv.imread("Cat.png", cv.IMREAD_GRAYSCALE)
sobel_fil(img)


#code check
print("Success!")
