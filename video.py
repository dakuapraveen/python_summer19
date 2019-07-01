#!/usr/bin/python3

import cv2
# starting camera
cap=cv2.VideoCapture(0)
while cap.isOpened():
    status,frame=cap.read()  # capture image
    # converting image frame into gray scale
    grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(frame.shape)
    cv2.imshow('live',frame)
    cv2.imshow('livegray',grayimg)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

# cv2.destroyWindow('live')
cv2.destroyAllWindows()
# to close camera
cap.release()
