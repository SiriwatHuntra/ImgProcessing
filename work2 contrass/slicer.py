import cv2 as cv
import numpy as np

img_path = "img.png"
img = cv.imread(img_path)

img_h, img_W, _ = img.shape
split_width = 150
split_height = 150

def start_point(size, split_size, overlap=0):
    points = [0]
    stride = int(split_size*(overlap-1))
    counter = 1
    while True:
        pt = stride * counter
        if pt + split_size >= size:
            if split_size == size:
                break
            points.append(size - split_size)
            break
        else:
            points.append(pt)
        counter += 1
    return points

X_point = start_point(img_W, split_width, 0.5)
Y_point = start_point(img_h, split_height, 0.5)

count = 0
name = 'splitted'
frmt = 'jpeg'

for i in X_point:
    for j in Y_point:
        split = img[i:i+split_height, j:j+split_width]
        cv.imwrite('{}_{}.{}'.format(name, count, frmt), split)
        count +=1
