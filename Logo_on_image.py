import numpy as np
import cv2

img1 = cv2.imread("img/jennifer.jpg")
img2 = cv2.imread("img/signature.bmp")

rows,cols,channels = img2.shape
print rows
print cols
print channels

roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 60, 255, cv2.THRESH_BINARY)
maskInv = cv2.bitwise_not(mask)

img1Bg = cv2.bitwise_and(roi, roi, mask)
img2Fb = cv2.bitwise_and(img2, img2, mask)

dst = cv2.add(img1Bg, img2Fb)
img1[0:rows,0:cols] = dst

cv2.imshow("win", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()