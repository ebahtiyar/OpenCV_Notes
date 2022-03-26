# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 22:19:54 2022

@author: emreb
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import warnings

def gaussianNoise(image):
    row,col,ch = image.shape
    
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy




warnings.filterwarnings("ignore")

img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255

plt.figure(),plt.imshow(img,cmap= "gray"),plt.axis("off"),plt.show()
img = gaussianNoise(img)

#Ortalama bulanıklaştırma

dst2 = cv2.blur(img,ksize = (3,3))

plt.figure()
plt.imshow(dst2,cmap= "gray"),plt.axis("off"),plt.show()

#gaussian blur
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure(),plt.imshow(gb,cmap= "gray"),plt.axis("off"),plt.show()

#medyan blur

mb= cv2.medianBlur(img, ksize = (3,3))
plt.figure(),plt.imshow(mb,cmap= "gray"),plt.axis("off"),plt.show()

