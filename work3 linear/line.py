import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), dtype='uint8')

def drawerLine():
    x1, y1 = map(int, input("Enter start point (x1, y1): ").split())
    start = (x1, y1)
    x2, y2 = map(int, input("Enter end point (x2, y2): ").split())
    end = (x2, y2)
    thick = int(input("Enter thickness: "))
    color = (255, 255, 255)
    cv.line(img, start, end, color, thick)
    return img

img = drawerLine()

cv.imwrite('line.jpeg', img)

cv.imshow('line', img)
cv.waitKey(0)
cv.destroyAllWindows()
