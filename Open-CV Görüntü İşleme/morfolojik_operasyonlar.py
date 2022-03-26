# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 15:18:40 2022

@author: emreb
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("datai_team.jpg",0)
plt.figure(),plt.imshow(img,cmap= "gray"),plt.axis("off"),plt.show()

#erozyon
kernel = np.ones((5,5) ,dtype = np.uint8)
result = cv2.erode(img,kernel,iterations = 1)
plt.figure(),plt.imshow(result,cmap= "gray"),plt.axis("off"),plt.show()

#genişleme dilation
result1 = cv2.dilate(img, kernel,iterations = 1)
plt.figure(),plt.imshow(result1,cmap= "gray"),plt.axis("off"),plt.show()

#whiteNoise 

whiteNoise = np.random.randint(0,2,size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(),plt.imshow(whiteNoise,cmap= "gray"),plt.axis("off"),plt.show()

noise_img =whiteNoise + img
plt.figure(),plt.imshow(noise_img,cmap= "gray"),plt.axis("off"),plt.show()

#açılma
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN ,kernel)
plt.figure(),plt.imshow(opening,cmap= "gray"),plt.axis("off"),plt.show()

#blackNoise 

blackNoise = np.random.randint(0,2,size = img.shape[:2])
blackNoise = whiteNoise*-255
plt.figure(),plt.imshow(blackNoise,cmap= "gray"),plt.axis("off"),plt.show()

black_noise_img =  blackNoise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(),plt.imshow(black_noise_img,cmap= "gray"),plt.axis("off"),plt.show()

closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(closing, cmap = "gray"), plt.axis("off"), plt.title("Kapama")

