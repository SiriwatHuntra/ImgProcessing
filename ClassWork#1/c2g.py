import cv2 as cv

# Load the color image
image = cv.imread('img1.png')

# Convert the color image to grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Display the color and grayscale images
cv.imshow('Color Image', image)
cv.imwrite('gimg.jpeg', gray_image)
cv.imshow('Grayscale Image', gray_image)
cv.waitKey(0)
cv.destroyAllWindows()
