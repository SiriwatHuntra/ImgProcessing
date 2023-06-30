img = cv.imread('dim.png', cv.IMREAD_GRAYSCALE)

img_out = cv.equalizeHist(img)

cv.imwrite('BEfore', img)
cv.imwrite('AFter', img_out)