import cv2 as cv
import numpy as np

def import_image_as_kernel(image_path):
    # Load the image
    kernel_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

    # Normalize the image to create the kernel
    kernel = kernel_image.astype(np.float32) / 255.0

    return kernel

# Example usage
kernel_path = 'line.jpeg'
kernel = import_image_as_kernel(kernel_path)

print("Kernel shape:", kernel.shape)
print("Kernel values:")
print(kernel)
