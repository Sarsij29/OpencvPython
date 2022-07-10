import cv2
import numpy as np

# ***** chapter 6 : Joining Images *******
def stackImages(scale, imgArray):
 rows = len(imgArray)
 cols = len(imgArray[0])
 rowsAvailable = isinstance(imgArray[0], list)
 width = imgArray[0][0].shape[1]
 height = imgArray[0][0].shape[0]
 if rowsAvailable:
  for x in range(0, rows):
   for y in range(0, cols):
    if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
    else:
     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
    if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
  imageBlank = np.zeros((height, width, 3), np.uint8)
  hor = [imageBlank] * rows
  hor_con = [imageBlank] * rows
  for x in range(0, rows):
   hor[x] = np.hstack(imgArray[x])
  ver = np.vstack(hor)
 else:
  for x in range(0, rows):
   if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
    imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
   else:
    imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
   if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
  hor = np.hstack(imgArray)
  ver = hor
 return ver

img=cv2.imread("Resouces/lena.png")
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgStack= stackImages(0.5,([img,img1,img],[img,img,img]))
# #img1=cv2.resize(img,(50,50))
# imgHor= np.hstack((img,img))  # there ar 2 issues with this method
# imgVer= np.vstack((img,img))  # 1. it cannot resize images to fulfill your requirement
#                                 2. it will not work on images with different channel i.e if 1 img is rgb and other is grayscale
# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)
cv2.imshow("Stack Images",imgStack)
cv2.waitKey(0)