import numpy as np
import cv2 as cv

haar_cascade =cv.CascadeClassifier('haar_face.xml')

people = [ 'MS Dhoni', 'Virat Kohli']

# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
 
img = cv.imread(r'D:\Program Files\PYTHON\Test 1\New folder\Dhoni.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('person',gray)
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 15)
for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    cv.rectangle(img, (x, y), (x+w,y+h), (0,255,255), thickness=2)
    print(f'label = {people[label]} with a confidence of {confidence}%')
    if confidence>70:
        
        cv.putText(img,str(people[label]), (x,y+20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), thickness=2)
    else:
        print('person not recognized')
        cv.putText(img,'person not recognised', (x,y+10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), thickness=2)
cv.imshow("image", img)
cv.waitKey(0)