# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import cv2 as cv
vc = cv.VideoCapture(0)  # 0 - 视频捕捉设备编号
while True:
    frame = vc.read()[1]
    cv.imshow('VideoCapture', frame)
    if cv.waitKey(33) == 27:  # 30 fps
        break
vc.release()
cv.destroyAllWindows()
