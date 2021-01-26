import cv2 as cv

img=cv.imread('../picture/cat_large.jpg')

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1] * scale)  #frame.shape[1] is width of frame
    height=int(frame.shape[0] * scale)  #frame.shape[0] is height of frame

    dimension = (width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

cv.imshow('Cat',img)
resized_img = rescaleFrame(img,scale=0.50)
cv.imshow('rescale_Cat',resized_img)
cv.waitKey(0)

