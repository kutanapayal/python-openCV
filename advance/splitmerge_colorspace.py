import cv2 as cv
import numpy as np

img=cv.imread('../picture/park.jpg')
cv.imshow('Park',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

#spllit the image
b,g,r = cv.split(img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

#it shows only shape of one color 
print(b.shape)
print(g.shape)
print(r.shape)

#color will disply as gray light has high intensity of given color.
cv.imshow("Blue",b)
cv.imshow("red",r)
cv.imshow("Green",g)


cv.imshow("Blue_Blue",blue)
cv.imshow("red_red",red)
cv.imshow("Green_Green",green)

merged=cv.merge([b,g,r])
cv.imshow('Merged',merged)

cv.waitKey(0)