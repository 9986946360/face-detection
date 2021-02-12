import numpy as np
import cv2
cpt = 0
maxFrames = 5

try:
    vidStream = cv2.VideoCapture(0)
except:
    print("problem opening input stream")
    sys.exit(1)

while cpt < maxFrames:
    ret, frame = vidStream.read()
    if not ret:
        sys.exit(0)
    cv2.imshow("test window",frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image',frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("image%04i.jpg" %cpt, frame)
    cv2.imwrite("image%04i.jpg" %cpt, frame)
    cpt += 1

    
