# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 21:34:39 2022

@author: emreb
"""

import cv2
import numpy as np
"""
img = cv2.imread("lenna.png",1)
print("Resim boytu:",img.shape)
cv2.imshow("Orginal",img)

imgResized = cv2.resize(img,(800,800))

print("Resized Img shape:",imgResized.shape)
cv2.imshow("Resized Img",imgResized)

imgCropped = img[:200,:300]
cv2.imshow("imgCropped",imgCropped)
"""

img = np.zeros((512,512,3),np.uint8)
print(img.shape)
cv2.imshow("Resim",img)

cv2.line(img,(0,0),(512,512),(255,255,0),3)
cv2.imshow("Resim_y",img)

cv2.rectangle(img, (0,0), (256,256), (255,0,0), cv2.FILLED)
cv2.imshow("Resim_kare",img)

cv2.circle(img,(300,300),45,(0,0,255))
cv2.imshow("Resim_çember",img)

cv2.putText(img, "Resim", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Metin", img)