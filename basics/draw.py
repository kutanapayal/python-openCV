import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#write the image a certain colour
blank[200:300,300:400]=0,0,255
cv.imshow("Green",blank)

#Draw a Rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)
cv.imshow('Rectangle',blank)

#Draw a Circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
cv.imshow('Circle',blank)

#draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
cv.imshow("Line",blank)

#write text
cv.putText(blank,'Hello! Text Demo',(0,300),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow("Text",blank)

cv.waitKey(0)