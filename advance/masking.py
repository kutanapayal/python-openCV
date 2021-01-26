#Masking use to focus on only parts of image and leave other

import cv2 as cv
import numpy as np

img = cv.imread('../picture/cats 2.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

#1) Circle
#--> Note: Mask size should not exceed the image size
mask=cv.circle(blank.copy(), (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask',mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked image',masked)

#2) Rectangle
mask2=cv.rectangle(blank.copy(), (30,30), (370,370),  255, -1)
cv.imshow('Mask 2',mask)

masked2 = cv.bitwise_and(img,img,mask=mask2)
cv.imshow('Masked image 2',masked2)

#3) Weird Shape
weird_shape = cv.bitwise_and(mask, mask2)
cv.imshow('Weird Shape',weird_shape)

masked3 = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shape Masked Image',masked3)

cv.waitKey(0)