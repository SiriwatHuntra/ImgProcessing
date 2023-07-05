import cv2 as cv
import random
import numpy as np

img = cv.imread("img1.png", cv.IMREAD_GRAYSCALE)
cv.imwrite("Original.png", img)

def seasoning(img):
    density_salt = 0.1
    density_pepper = 0.1

    #set salt pix
    number_of_salt = int(density_salt * (img.shape[0] * img.shape[1]))

    #add some salt
    for i in range(number_of_salt):
        y_coord = random.randint(0, img.shape[0]-1)
        x_coord = random.randint(0, img.shape[1]-1)
        img[y_coord][x_coord] = 255

    #set salt pix
    number_of_pepper = int(density_pepper * (img.shape[0] * img.shape[1]))

    #add some salt
    for i in range(number_of_pepper):
        y_coord = random.randint(0, img.shape[0]-1)
        x_coord = random.randint(0, img.shape[1]-1)
        img[y_coord][x_coord] = 0
    return img

# import module
from PIL import Image, ImageChops
def compareter():

    # assign images
    img1 = Image.open("Original.png")
    img2 = Image.open("medien.png")

    # finding difference
    diff = ImageChops.difference(img1, img2)

    # showing the difference
    diff.show()
    diff.save("compared_img.png")

def percentage_check():
    img = cv.imread("compared_img.png")
    number_of_white_pix = np.sum(img == 255)
    pix_sum = np.sum(img)
    print(number_of_white_pix,"/",pix_sum)
    persentage = (number_of_white_pix/pix_sum)*100

    return print('Error in persentage is:', persentage)

sp_img = seasoning(img)
cv.imwrite("sp_img.png", sp_img)

median = cv.medianBlur(sp_img, 5)

cv.imwrite("medien.png", median)

img = cv.imread("Original.png")

compareter()
percentage_check()
