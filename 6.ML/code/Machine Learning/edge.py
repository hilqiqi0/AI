# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import cv2 as cv
original = cv.imread('../../data/chair.jpg')
cv.imshow('Original', original)
canny = cv.Canny(original, 50, 240)
cv.imshow('Canny', canny)
cv.waitKey()
