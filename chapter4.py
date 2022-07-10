import cv2
import numpy as np
#   ************** CHAPTER 4: sHAPES AND TEXTS *******************

img=np.zeros((512,512,3),np.uint8)
#print(img.shape)
#print(img)
#img[:]=255,0,0 # bgr format of image coloring
#img[0:200,100:350]=255,0,0 # img[height,width]

#cv2.line(img,(0,0),(300,300),(0,255,0),5) #cv2.line(img,start pt,end pt,color,thickness of line)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),1)
#cv2.rectangle(img,(0,0),(250,350),(0,0,255),2) # same as line but in place of endpt u give diagonal pt
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,255,0),3) #cv2.circle(img,center,radius,color,thickness)
cv2.putText(img,"*OPENCV*",(250,200),cv2.FONT_ITALIC,1.5,(0,150,0))

cv2.imshow("Image",img)
cv2.waitKey(0)