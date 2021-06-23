import cv2
import handtrackingmodule as htm
import time
import numpy as np
import math

cam = cv2.VideoCapture(0)
detector = htm.Handdetector(detectionconf=0.75)

while(cam.isOpened()):
    _,img = cam.read()
    img = cv2.flip(img,1)
    img = detector.findhands(img)
    lmlist = detector.findposition(img,draw=False)
    c = 0
    for i in range(8,21,4):
        try:
            if lmlist[i][2]<lmlist[i-1][2] or lmlist[i][2]<lmlist[i-2][2]:
                c+=1
        except:
            pass
    try:
        if lmlist[4][1] < lmlist[3][1]:
            c+=1
    except:
        pass
    cv2.putText(img,f"fingesr = {c}",(10,70),cv2.FONT_ITALIC,2,(255,0,0),2) 
    cv2.imshow('w',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
# print(m1,m2)

cam.release()
cv2.destroyAllWindows()