# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:42:03 2022

@author: emreb
"""

import cv2
import numpy as np
img = cv2.imread("lenna.png",1)
cv2.imshow("Orginal:",img)

hor = np.hstack((img,img))
cv2.imshow("Hor",hor)

ver = np.vstack((img,img))
cv2.imshow("Dikey",ver)