import cv2
import matplotlib.pyplot as plt

img = cv2.imread("odev1.jpg",0)

plt.figure(),plt.imshow(img,cmap= "gray"),plt.axis("off")

print(img.shape)

imresized = cv2.resize(img,(int(img.shape[1]*4/5),int(img.shape[0]*4/5)))
plt.figure(),plt.imshow(imresized,cmap= "gray"),plt.axis("off")
print(imresized.shape)        

      

cv2.putText(img, "Kopek", (450,120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
plt.figure(),plt.imshow(img,cmap= "gray")

img = cv2.imread("odev1.jpg")
_,thresh_img = cv2.threshold(img,thresh = 50, maxval = 255, type = cv2.THRESH_BINARY)
cv2.imshow('thresh_img ', thresh_img )

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
cv2.imshow('gb ', gb )

img = cv2.imread("odev1.jpg",0)
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_64F)
cv2.imshow('Laplacian', laplacian)

img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure()
plt.plot(img_hist)














