# based on https://python-mss.readthedocs.io/examples.html#opencv-numpy

import cv2
import numpy
import mss
import time

with mss.mss() as sct:
    # monitor = {'top': 0, 'left': 0, 'width': 800, 'height': 640}

    while True:
        time.sleep(3)
        img = numpy.array(sct.grab(sct.monitors[1]))
        cv2.imshow("screen grab test", img)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

        g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # make black and white image b
        #cv2.imshow('bw', b)

        time.sleep(120)
        

    # cv2.destroyAllWindows()