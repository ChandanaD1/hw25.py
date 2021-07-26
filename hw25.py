# background matters

import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

image = cv2.imread("bg.png")

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

frame = cv2.resize(hsv, (640,480))
image = cv2.resize(image, (640,480))

lower_black = np.array([104,153,70])
upper_black = np.array([30,30,0])

mask = cv2.inRange(frame,lower_black,upper_black)
res= cv2.bitwise_and(frame, frame, mask=mask)

f = frame - res
f = np.where(f==0,image,f)

cap.release()
cv2.destroyAllWindows()
