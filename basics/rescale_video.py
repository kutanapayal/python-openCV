import cv2 as cv

capture=cv.VideoCapture('../videos/dog.mp4')   # 0 or 1 or 2 if youu want to give reference to your webcam

# it works with image and videos(static & live) 
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1] * scale)  #frame.shape[1] is width of frame
    height=int(frame.shape[0] * scale)  #frame.shape[0] is height of frame

    dimension = (width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

#work only on Live videos
def changeResolution(width,height):
    capture.set(3,width)
    capture.set(4,height)

while True:
    #it will Shows video
    isTrue,frame = capture.read()
    resized_frame = rescaleFrame(frame)

    cv.imshow('Video',frame)
    cv.imshow('rescale Video',resized_frame)

    #way to break out of while loop
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


