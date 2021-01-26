import cv2 as cv
import numpy as np

img = cv.imread('..\picture\park.jpg')

cv.imshow('park',img)

#translation
def translate(img, x , y):
    transMat= np.float32([[1,0,x],[0,1,y]])
    dimensions= (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

#-x--> left
#-y--> up
#x--> right
#y--> down

translated = translate(img, -100, -100)
cv.imshow('Translated',translated)


#Rotation    
def rotate(img, angle, rotaionPoint=None):
    (height,width) = img.shape[:2]

    if rotaionPoint is None:
        rotaionPoint = (width//2, height//2)    
    
    rotaionMat = cv.getRotationMatrix2D(rotaionPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotaionMat, dimensions)

rotated = rotate(img, -45)      # -45 means clockwise , 45 it would be anticlockwise
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -45) # try using original img with 90 degree & analyze the output
cv.imshow('Rotated rotated',rotated_rotated)

#Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Flipping
# 0--> Flip img vertically on X axis
# 1--> Flip img horizontally on Y axis
# -1--> Flip img vertically and horizontally  on X-Y axis
flip = cv.flip(img, -1)
cv.imshow('Flip',flip)

#Cropping
cropped = img[100:400, 300:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)