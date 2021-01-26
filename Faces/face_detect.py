#Detect Faces Using HaarCascade
import cv2 as cv

img = cv.imread('../picture/group 1.jpg')
cv.imshow('Person',img)

#We use haar_face.xml as our classifier for detecting face in our image

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person',gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

#by changing values you can make it scalable
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)    

print(f'Number of faces found = {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w,y+w), (0,255,0), thickness=2)

cv.imshow('Detected Faces',img)

cv.waitKey(0)