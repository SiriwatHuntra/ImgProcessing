import cv
import numpy as np

import numpy as np

def draw_line(image, start, end, color=255):
    x0, y0 = start
    x1, y1 = end
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        image[y0, x0] = color
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    return image

def convolute_image(image, kernel_image):
    kernel_sum = kernel_image.sum()
    kernel = kernel_image.astype(np.float32) / kernel_image.sum()
    conv = cv.filter2D(src=image, ddepth=-1, kernel=kernel)
    return conv

image = cv.imread('image.png', cv.IMREAD_GRAYSCALE)
cv.imshow('original', image)

line_image = np.zeros((512, 512), dtype='uint8')

start = (10, 10)
end = (20, 20)
line_image = draw_line(line_image, start, end)
cv.imwrite('line.jpeg', line_image)
cv.imshow('line', line_image)

conv = convolute_image(image, line_image)

cv.imshow('image', conv)
cv.imwrite('solution.jpeg', conv)
cv.waitKey(0)
cv.destroyAllWindows()
