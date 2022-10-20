# based on https://python-mss.readthedocs.io/examples.html#opencv-numpy

import cv2
import numpy
import mss
import time
import imutils
import matplotlib.pyplot as plt

with mss.mss() as sct:
    # monitor = {'top': 0, 'left': 0, 'width': 800, 'height': 640}

    while True:
        time.sleep(3)
        img = numpy.array(sct.grab(sct.monitors[1]))
        cv2.imshow("screen grab test", img)

        g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray', g)

        f = cv2.bilateralFilter(g, 11, 17, 17)

        e = cv2.Canny(f, 30, 200)
        cv2.imshow("canny", e)

        cv2.imwrite('canny.png', e)

        # e2 = e.copy()

        # keypoints = cv2.findContours(e2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # #contours = imutils.grab_contours(keypoints)
        # for contour in keypoints:
        #     cv2.drawContours(e2, contour, -1, (0, 255, 0), 3)
        
        #cv2.imshow('contours', e2)




        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        
        time.sleep(120)

    # cv2.destroyAllWindows()