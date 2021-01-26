#thresholding means binarization of image
import cv2 as cv
import numpy as np

img = cv.imread('../picture/cats.jpg')
cv.imshow('Cat',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#1) simple Thresholding --> intensity above 150 assign 255 else 0.
threshold,thresh = cv.threshold(gray, 150 ,255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded',thresh)

#Inverse --> intensity above 150 assign 0 else 255.
threshold,thresh_inv = cv.threshold(gray, 150 ,255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded - Inverse',thresh_inv)

#2) Adaptive Thresholding --> no threshold value , depends on mean of (13,13) mask and 5 subtracted from mean to scale it better way.
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 13, 5)
cv.imshow('Adaptive Thresholded',adaptive_thresh)

#Inverse  --> Gaussian add weight to each pixel to get better filtered image 
adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adaptive Thresholded - Inverse',adaptive_thresh_inv)

cv.waitKey(0)

