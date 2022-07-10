import cv2
import numpy as np
#  VIRTUAL PAINT ##############
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0) # 0 is for inbuilt webcam and 1 is for external webcams
cap.set(3,frameWidth) # 3 sets the width or length
cap.set(4,frameHeight) # 4 set the height or bredth
cap.set(10,150) # 10 is for brightness

myColors = [[6,203,116,39,255,255],  # orange 5,107,0,19,255,255
             [142,154,41,169,237,198],  # magenta 133,56,0,159,156,255
             [60,150,28,87,255,255], #Green
            [43,117,90,133,255,212]] # blue
myColorValues=[[51,153,255],[219,60,198],[97,164,20],
               [255,51,51]]

myPoints = []
newPoints = []

def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count=0
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask=cv2.inRange(imgHSV,lower,upper)
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
        #cv2.imshow(str(color),mask)
    return newPoints


def getContours(img):
    contours,heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area>=80:
            #cv2.drawContours(imgResult,cnt,-1,(255,168,12),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0],point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult=img.copy()
    newPoints=findColor(img,myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)


    cv2.imshow("Video",imgResult)
    if cv2.waitKey(1) & 0xFF ==ord('q') :
        break
