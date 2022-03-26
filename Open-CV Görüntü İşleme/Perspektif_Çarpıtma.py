# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:47:12 2022

@author: emreb
"""

import cv2
import numpy as np

img = cv2.imread("kart.png")

cv2.imshow("Orginal",img)

width = 400
height = 500

pts1 = np.float32([[230,1],[1,472],[540,150],[338,617]]) #paintten baktık
pts2 = np.float32([[0,0],[0, height],[width,0],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

imgOutput = cv2.warpPerspective(img, matrix, ((width,height)))

cv2.imshow("Sonuc",imgOutput)