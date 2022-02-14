import numpy as np
import cv2
import time
import threading
from defs import *

tm = True

cap = cv2.VideoCapture(1)
rc_cascade = cv2.CascadeClassifier('cascade2.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rcs = rc_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h,) in rcs:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+w, x:x+w]

        xmid = (w/2+x)
        ymid = (h/2+y)

        t = threading.Thread(target=lr).start()
        t = threading.Thread(target=ud).start()
        t = threading.Thread(target=sd).start()
        t = threading.Thread(target=xlp).start()
        t = threading.Thread(target=ylp).start()
        t = threading.Thread(target=lp).start()

        if ymid > 48 or ymid < 432 and xmid > 160 or xmid < 480:
            if tm == True:
                t = threading.Thread(target=wait).start()
                tm = False
                t = threading.Thread(target=times).start()

    tlframe = cv2.line(frame, (160, 48), (160, 432), (154, 0, 210), (5))
    trframe = cv2.line(frame, (480, 48), (480, 432), (154, 0, 210), (5))
    tuframe = cv2.line(frame, (160, 48), (480, 48), (154, 0, 210), (5))
    tdframe = cv2.line(frame, (160, 432), (480, 432), (154, 0, 210), (5))

    olframe = cv2.line(frame, (0, 0), (0, 480), (0, 90, 0), (5))
    odframe = cv2.line(frame, (0, 480), (640, 480), (0, 90, 0), (5))
    ouframe = cv2.line(frame, (0, 0), (640, 0), (0, 90, 0), (5))
    orframe = cv2.line(frame, (640, 0), (640, 480), (0, 90, 0), (5))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()