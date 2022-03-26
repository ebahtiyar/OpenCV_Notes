# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 22:07:08 2022

@author: emreb
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img,cmap= "gray")
plt.axis("off")
plt.show()

_,thresh_img = cv2.threshold(img,thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_img,cmap= "gray")
plt.axis("off")
plt.show()

#uyarlamalı eşik değer

thresh_img1 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,8)

plt.figure()
plt.imshow(thresh_img1,cmap= "gray")
plt.axis("off")
plt.show()