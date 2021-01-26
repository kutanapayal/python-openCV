import cv2 as cv
import numpy as np

img = cv.imread('../picture/park.jpg')
cv.imshow('Cat',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Laplacian Edges
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian Edges',lap)

#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)  # --> it will fetch all edges abt the x-axis (Horizontally)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)  # --> it will fetch all edges abt the y-axis (Vertically) 
combined_sobel=cv.bitwise_or(sobelx,sobely) # --> Sobel Edges

cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('Combine sobel',combined_sobel)

#Canny --> More Cleaner Version for Compute gradient
#canny is multiple stage process -> it uses sobel one of it's step
canny=cv.Canny(gray, 150, 175)
cv.imshow('Canny',canny)

cv.waitKey(0)