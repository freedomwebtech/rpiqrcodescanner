import cv2
import numpy as np
import pyzbar.pyzbar as qr

cap=cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
      ret,frame = cap.read()
      flipped = cv2.flip(frame, flipCode=-1)
      frame1=cv2.resize(flipped,(640,480))
      qrdetect=qr.decode(frame1)

     
      for i in qrdetect:
          print (i.rect.left,i.rect.top,i.rect.width,i.rect.height)
          print (i.data)
          cv2.rectangle(frame1,(i.rect.left,i.rect.top),(i.rect.left+i.rect.width,i.rect.top+i.rect.height),(0,255,0),3)
          cv2.putText(frame1,str(i.data),(20,20),font,2,(255,0,0),2) 
      cv2.imshow("Frame", frame1)
      key = cv2.waitKey(1) & 0xFF
      if key == ord("q"):
         break
        