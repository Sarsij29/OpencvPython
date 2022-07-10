import cv2
import numpy as np

# DOCUMENT SCANNER ###
#################################
widthImg=640
heightImg=480
#####################################
cap = cv2.VideoCapture(0) # 0 is for inbuilt webcam and 1 is for external webcams
cap.set(3,widthImg) # 3 sets the width or length
cap.set(4,heightImg) # 4 set the height or bredth
cap.set(10,100) # 10 is for brightness


def preProcessing(img):
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny=cv2.Canny(imgBlur,200,200)
    kernel= np.ones((5,5))
    imgDialation=cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres = cv2.erode(imgDialation,kernel,iterations=1)

    return imgThres

def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours, heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 5000:
            #cv2.drawContours(imgContour,cnt,-1,(255,168,12),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            if area>maxArea and len(approx)==4:
                biggest=approx
                maxArea=area

    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    return biggest


def getWarp(img,biggest):
    pass


while True:
    success, img = cap.read()

    cv2.resize(img,(widthImg,heightImg))
    imgContour = img.copy()
    imgThres=preProcessing(img)
    biggest=getContours(imgThres)
    print(biggest)
    getWarp(imgContour,biggest)

    cv2.imshow("Result",imgContour)
    if cv2.waitKey(1) & 0xFF ==ord('q') :
        break
