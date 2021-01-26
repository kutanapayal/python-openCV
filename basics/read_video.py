import cv2 as cv

capture=cv.VideoCapture('../videos/dog.mp4')   # 0 or 1 or 2 if youu want to give reference to your webcam

while True:
    #it will Shows video
    isTrue,frame = capture.read()
    cv.imshow('Video',frame)

    #way to break out of while loop
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
