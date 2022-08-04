import cv2 as cv
img = cv.imread('Screenshot_2022-07-31-20-25-19-09_680d03679600f7af0b4c700c6b270fe7.jpg ')
gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
haar_cascade =cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbours=3)

print(f'no of faces found ={len(faces_rect)}')
for (x,y,w,h) in faces_rect:
     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('Detfaces',img)

