#recognize faces using open_cv build in face recognizer
import os
import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')
people = []
for i in os.listdir(r'C:\Users\LENOVO\Desktop\Bacancy\python_opencv\people_faces'):
    people.append(i)
#features = np.load('features.npy',allow_pickle=True)
#labels = np.load('labels.npy')

#instantiate recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img=cv.imread(r'C:\Users\LENOVO\Desktop\Bacancy\python_opencv\people_faces\second\3.jpg')

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

#Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label,confidence = face_recognizer.predict(faces_roi)
    print(f'label= {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face',img)
cv.waitKey(0)