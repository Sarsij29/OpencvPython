import cv2
import numpy as np
# Chapter 5 : WARP perspective  ********

img = cv2.imread("Resouces/cards.png")

width, height = 250,350
pts1 = np.float32([[195,452],[420,380],[291,776],[522,702]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Warp Image",imgOutput)
cv2.waitKey(0)