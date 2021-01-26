import os
import numpy as np
import cv2 as cv

people = []
for i in os.listdir(r'C:\Users\LENOVO\Desktop\Bacancy\python_opencv\people_faces'):
    people.append(i)

print(people)
DIR = r'C:\Users\LENOVO\Desktop\Bacancy\python_opencv\people_faces'
haar_cascade = cv.CascadeClassifier('haar_face.xml')

features=[]
labels=[]

def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print(f'len of features {len(features)}')
print(f'len of labels {len(labels)}')

print("Training done --------------")
features = np.array(features, dtype='object')
labels = np.array(labels)

#instantiate recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train the Recognizer on the features list and the label list
face_recognizer.train(features,labels)

#we can use this face recognizer in other files creating yml file
face_recognizer.save('face_trained.yml')

np.save('features.npy',features)
np.save('labels.npy',labels)