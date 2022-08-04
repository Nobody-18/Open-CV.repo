import cv2 as  cv
def resized_frame(frame,scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Southhall.mp4')
while True:
    isTrue,frame=capture.read()
    resized =resized_frame(frame)
    cv.imshow('video',resized)
    if cv.waitKey(20) &0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()    