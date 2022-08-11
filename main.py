import numpy as np
import cv2  
import time

cap = cv2.VideoCapture(0)
timer_running = False
xg=0

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([40,40,70])
    upper_green = np.array([80,255,255])
    mask = cv2.inRange (hsv, lower_green, upper_green)
    greencontours = cv2.findContours(mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(greencontours)>0:
        green_area = max(greencontours, key=cv2.contourArea)
        (xg,yg,wg,hg) = cv2.boundingRect(green_area)
        cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)
    frame = cv2.line(frame, (400, 0), (400, 600), (0, 255, 0), 2)
    frame = cv2.line(frame, (300, 0), (300, 600), (255, 0, 0), 2)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)


    if timer_running == False:
        
        if xg > 390 and xg < 410:
            print("stopwatch is running")
            start_time = time.time()
            timer_running = True
    if timer_running == True:
        if xg > 290 and xg < 310:
            print("time: ", time.time() - start_time)
            break

    k = cv2.waitKey(5) 
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
