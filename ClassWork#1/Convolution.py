import cv2
import numpy as np

def draw_line(image, start, end, color=(255, 255, 255), thickness=2):
    image = cv2.line(image, start, end, color, thickness)
    return image

def convolute(image, kernel):
    image = cv2.filter2D(image, -1, kernel)
    return image

image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
line_image = np.zeros((512, 512), dtype='uint8')
line_image = draw_line(line_image, (0, 0), (100, 100))

kernel = np.ones((5,5),np.float32)/25
convoluted_image = convolute(line_image, kernel)

cv2.imshow('image', convoluted_image)
cv2.imwrite('solution.jpeg', convoluted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
