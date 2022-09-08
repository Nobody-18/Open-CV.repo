from ctypes import c_void_p
import os 
import cv2 as cv 
import numpy as np
people = ['MS Dhoni', 'Virat Kohli']
DIR = r'D:\Program Files\PYTHON\Test 1\New folder (2)'
haar_cascade =cv.CascadeClassifier('haar_face.xml')
features = []
labels = []
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_arr = cv.imread(img_path)
            gray = cv.cvtColor(img_arr, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1)
            for (x,y,w,h ) in faces_rect:
                faces_rof = gray[y:y+h,x:x+w]
                features.append(faces_rof)
                labels.append(label)


create_train()
print(f'done  training')
features = np.array(features, dtype='object')
labels = np.array(labels)
face_recognizer = cv.face.LBPHFaceRecognizer_create()
# train the recognizer on the features and labels
face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)