import cv2 as cv

img=cv.imread('../picture/cats.jpg')
cv.imshow('Cats',img)

#Averaging
average = cv.blur(img, (7,7))
cv.imshow('Average Blur',average)

#Gaussian Blur
gauss= cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur',gauss)

#Median Blur
median= cv.medianBlur(img, 5)
cv.imshow('Median Blur',median)

#Bilateral
bilateral=cv.bilateralFilter(img, 10, 35, 25)   #increasing value means washedout look
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)