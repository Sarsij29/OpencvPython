import cv2
import numpy as np


# chapter 1: Reading images, videos and web cameras---------------
# ******* image ****************
# print("package imported")
#
# img = cv2.imread("Resouces/lena.png")
#
# cv2.imshow("Output",img)
# cv2.waitKey(0)

#  ************** video ***********
# cap = cv2.VideoCapture("Resouces/test_video.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q') :
#         break


# ************* webcam capture *****************
# cap = cv2.VideoCapture(0) # 0 is for inbuilt webcam and 1 is for external webcams
# cap.set(3,680) # 3 sets the width or length
# cap.set(4,480) # 4 set the height or bredth
# cap.set(10,100) # 10 is for brightness
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q') :
#         break

# Chapter 2: some basic functions *****************
# img = cv2.imread("Resouces/lena.png")
# kernel=np.ones((5,5),np.uint8) #kernel is a matrix , matrix of 1s with unsigned integer of 8 bits
#
#
# imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur=cv2.GaussianBlur(imgGray,(19,19),0)
# imgCanny=cv2.Canny(img,150,150) # for showing edges in an image
# imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) # for dialating those edges
# imgEroded = cv2.erode(imgDialation,kernel,iterations=1) # opposite of dialating
#
# #cv2.imshow("Image",img)
# cv2.imshow("Gray Image",imgGray)
# cv2.imshow("Blur Image",imgBlur)
# cv2.imshow("Canny Image",imgCanny)
# cv2.imshow("Dialation Image",imgDialation)
# cv2.imshow("Eroded Image",imgEroded)
# cv2.waitKey(0)


### chapter 3: Image resize and crop *******************************
img = cv2.imread("Resouces/lambo.jpg")
print(img.shape)
imgResize= cv2.resize(img,(400,500)) # first width is given and then height is given
# image is nothing but array or matrix of pixels
imgCropped=imgResize[0:300,100:400]
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
cv2.waitKey(0)