import cv2 as cv

img = cv.imread('../picture/cat.jpg')

cv.imshow('Cat',img)

#Converting image to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge cascade
canny=cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

#Dilating the image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

#Eraing
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)

#resize
resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resize',resize)

#Crop image
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)