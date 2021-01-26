import cv2 as cv
import numpy as np

img = cv.imread('../picture/cats.jpg')
cv.imshow('Cat',img)

blank = np.zeros(img.shape, dtype='uint8') 
cv.imshow('Blank',blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny',canny)

ret , thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Tresh',thresh)

#1)cv.RETR_EXTERNAL --> edges outside of hierarchies, 2)cv.RETR_TREE --> edges inside of hierarchies 3)cv.RETR_LIST -->all edges
#1)cv.CHAIN_APPROX_SIMPLE--> give compresses edges ,2)cv.CHAIN_APPROX_NONE --> all co-ordinates
contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)  #u can find contour on thresh also.
print(f'{len(contours)} contours(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)