import cv2
import numpy
import mss
import time
import imutils
import matplotlib.pyplot as plt

canny = cv2.imread('canny.jpg')
cv2.imshow('canny', canny)
canny = cv2.cvtColor(canny, cv2.COLOR_BGR2GRAY)
canny2 = canny.copy()
canny2 = cv2.cvtColor(canny2, cv2.COLOR_GRAY2RGB)

keypoints = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
for contour in contours:
    cv2.drawContours(canny2, contour, -1, (0, 255, 0), 3)

canny2 = cv2.resize(canny2, (int(canny2.shape[1] * 0.6), int(canny2.shape[0] * 0.6)))
cv2.imshow('contours', canny2)

key = cv2.waitKey(0)
    