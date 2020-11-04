#import curses
import numpy as np
import time
import cv2
from gpiozero import Robot

robot = Robot(left=(17, 22), right=(23, 24))

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()

rec.read("recognizer/trainningData.yml")
id = 0
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

 ret, img = cam.read()
 gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 faces = faceDetect.detectMultiScale(gray,1.3,5)

 for (x,y,w,h) in faces:
     cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
     id, conf = rec.predict(gray[y:y+h, x:x+w])

     if id==1:
         id = "josh"

         robot.forward()
         time.sleep(1)
         robot.stop()
         time.sleep(5)
         robot.backward()
         time.sleep(1)
     
     else :
         robot.stop()
         #GPIO.output(Buzzer, 1)
         ##time.sleep(5)
     cv2.putText(img, str(id), (x,y+h),font,2, (255,0,0),1,cv2.LINE_AA)
 cv2.imshow("face", img)
     

 id = 0 
 if cv2.waitKey(1)==ord('q'):
       break

cam.release()
cv2.destroyAllWindows()