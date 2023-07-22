import cv2
import numpy as np
from matplotlib import pyplot as plt

def show_image(image, title=''):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def sobel_filter(image):
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    return sobel_x

# 1) Create a horizontal Sobel Filter and show the result
input_image = cv2.imread('Cat.png', 0)
sobel_filtered_image = sobel_filter(input_image)
show_image(sobel_filtered_image, 'Sobel Filter Result')

# 2) Transform the Input image into the Frequency Domain with Fourier Transform and save the result
input_fft = np.fft.fftshift(np.fft.fft2(input_image))
magnitude_spectrum_input = 20 * np.log(np.abs(input_fft))
cv2.imwrite('frequency_input.jpg', magnitude_spectrum_input)

# 3) Transform the Sobel Filtered image into the Frequency Domain with Fourier Transform and save the result
sobel_fft = np.fft.fftshift(np.fft.fft2(sobel_filtered_image))
magnitude_spectrum_sobel = 20 * np.log(np.abs(sobel_fft))
cv2.imwrite('frequency_sobel.jpg', magnitude_spectrum_sobel)

# 4) Multiply Input and Sobel Filtered images in the Frequency Domain point by point (Dot Product) and save the result 
result_fft = np.multiply(input_fft, sobel_fft)
result_image = np.fft.ifft2(np.fft.ifftshift(result_fft))
result_image = np.abs(result_image)
result_image = cv2.normalize(result_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
cv2.imwrite('result_frequency.jpg', result_image)

# 5) Convert the resulting image back to the Spatial Domain and save the result
result_spatial = np.fft.ifft2(result_fft)
result_spatial = np.abs(result_spatial)
result_spatial = cv2.normalize(result_spatial, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
cv2.imwrite('result_spatial.jpg', result_spatial)

# Show the resulting images
show_image(magnitude_spectrum_input, 'Frequency Domain (Input Image)')
show_image(magnitude_spectrum_sobel, 'Frequency Domain (Sobel Filter)')
show_image(result_image, 'Result (Frequency Domain)')
show_image(result_spatial, 'Result (Spatial Domain)')
