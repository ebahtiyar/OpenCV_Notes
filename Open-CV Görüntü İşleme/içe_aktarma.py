# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:49:31 2022

@author: emreb
"""

import cv2
import time
#Resim içe aktarma
img = cv2.imread("messi5.jpg",0)
cv2.imshow("ilk resim",img)

k = cv2.waitKey(0) &0xFF

if k == 27: #escq
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("messi_gray.png",img)
    cv2.destroyAllWindows()
    
#Video içe aktarma
    
video_name = "MOT17-04-DPM.mp4"

cap = cv2.VideoCapture(video_name)

print("Genişlik",cap.get(1))
print("Yükselik",cap.get(4))

if not cap.isOpened():
    print("Hata")
    
while True:
    ret , frame = cap.read()
    if ret:
        time.sleep(0.01)
        cv2.imshow("Video",frame)
    else: break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()    
cv2.destroyAllWindows()