#!/usr/bin/python3

import cv2
# starting camera
cap=cv2.VideoCapture(0)
r=cap.isOpened()
print(r)      # print status
status,frame=cap.read()  # capture image
cv2.imshow('live',frame)
cv2.waitKey(0)  # wait the window
