import cv2 as cv
img=cv.imread('Batman.png')
def resized_frame(frame,scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
#cv.imshow('Batman',img)
img=resized_frame(img)
#cv.imshow('small',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gary',gray)
cv.imshow('nil',img)

cv.waitKey(0)