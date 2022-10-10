import numpy as np
import cv2 as cv
import os 

haar_cascade =cv.CascadeClassifier('haar_face.xml')

people = [ 'MS Dhoni', 'Virat Kohli']

# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
count = 1
DIR = r'D:\ProgramFiles\PYTHON\Test 1\New folder'
for img in os.listdir(DIR):
    img_path = os.path.join(DIR,img)

    imga = cv.imread(img_path)
    gray = cv.cvtColor(imga, cv.COLOR_BGR2GRAY)
    # cv.imshow('person',gray)
    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 5)
    
    for (x, y, w, h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)
        cv.rectangle(imga, (x, y), (x+w,y+h), (0,255,255), thickness=2)
       
        print(f'{count}.label = {people[label]} with a confidence of {confidence}%')
       
        # if confidence>70:
        
        cv.putText(imga,str(people[label]), (x,y+20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), thickness=2)
        # else:
        #     print('person not recognized')
        #     cv.putText(img,'person not recognised', (x,y+10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), thickness=2)
    cv.imshow("image", imga)
    count += 1
    cv.waitKey(1000)

