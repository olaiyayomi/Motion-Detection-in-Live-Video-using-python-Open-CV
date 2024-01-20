import cv2 as cv
import sys
import numpy as np
import os

video = cv.VideoCapture(0)

if not video.isOpened():
    sys.exit("unable to locate camera, try fixing your camera first")

def capture():
    __, frame1 = video.read()
    cv.imwrite("D:/YOMTECH PROJECTS/my python/test/real_image.png", frame1)

i = 0
    
while True:
    ret, frame = video.read()
    #print(frame.shape)
    blue, green, red = frame[100,100]
    
    iblue = 67
    
    if os.path.exists("D:/YOMTECH PROJECTS/my python/test/real_image.png"):
        img = cv.imread("D:/YOMTECH PROJECTS/my python/test/real_image.png")
        
        iblue, igreen, ired = img[100,100]
        
        
    fblue, fgreen, fred = frame[100,100]
    
    if fblue != iblue:
        i = i+1
        print("Something was detected from your in your camera", i)
    
    
    cv.circle(frame, (100,100), 9, 255, 3)
    
        
    cv.imshow("my video", frame)
    key = cv.waitKey(1)
    
    if key == ord("c"):
        capture()
        
    if key == ord("q"):
        break
cv.destroyAllWindows()
video.release()
