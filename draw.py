import cv2 as cv 
import numpy as np
img=cv.imread('Batman.png')
#cv.imshow('Batman',img)
blank=np.zeros((500,500,3),dtype='uint8')
blank[:]=0,0,255
blank[200:300,300:400]=0,0,0
cv.rectangle(blank,(300,400),(200,300),(255,255,255),thickness=12)
cv.circle(blank,(250,250),50,(0,255,255),thickness=5)
blank1=np.zeros((500,500,3),dtype='uint8')
cv.line(blank1,(0,250),(500,250),(255,0,0),thickness=12)
cv.putText(blank1,'hello',(0,250),cv.FONT_HERSHEY_COMPLEX,2,(255,255,255),2)
#cv.imshow('Blank',blank)
cv.imshow('Blank1',blank1)
cv.waitKey(0)