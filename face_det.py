import cv2 as cv

img = cv.imread('D:\Program Files\GITHUB\Open-CV.repo\group.jpeg')
# cv.imshow('batman',img)

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gary',gray)
haar_cascade =cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1)

print(f'no of faces found ={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('Detfaces',img)
cv.waitKey(0)

