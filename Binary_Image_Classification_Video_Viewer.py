from collections import deque
import numpy as np
import cv2
filename = 'Video_CV_Project\MOVI00'
num = '07'
filetype = '.avi'
cap = cv2.VideoCapture(filename+num+filetype)
Last100 = deque()
framecount = 0
Toggle = True
Tempframe = 0
while (cap.isOpened()):
    testingthing = cv2.waitKey(1)
    if (testingthing & 0xFF == ord(' ')):
        Toggle = not Toggle
    if (Toggle):
        if (Tempframe == 0): # If we are in real time
            framecount = framecount + 1
            print(framecount)
            ret, frame = cap.read() #reads 1 frame, presumably
            if (frame is None):
                print("Done!")
                exit()
            cv2.imshow('frame', frame)
            Last100.append(frame)
        elif (Tempframe > 0):
            print("FUCK")
        else: # If we are in the previous 100 frames
            Tempframe = Tempframe + 1
            print(framecount + Tempframe, ":", Tempframe)
            if (Tempframe != 0):
                cv2.imshow('frame', Last100[100+Tempframe])
    if (not Toggle):
        if (testingthing & 0xFF == ord('o')):
            Tempframe = len(Last100) * -1
            print(framecount + Tempframe)
            cv2.imshow('frame', Last100[100+Tempframe])

        if (testingthing & 0xFF == ord('l')):
            if (Tempframe < -1):
                Tempframe = Tempframe + 1
                print(framecount + Tempframe, ":", Tempframe)
                cv2.imshow('frame', Last100[100+Tempframe])
            else:
                framecount = framecount + 1
                print(framecount)
                ret, frame = cap.read() #reads 1 frame, presumably
                cv2.imshow('frame', frame)
                Last100.append(frame)
    while (len(Last100) > 100):
            Last100.popleft()
    if (testingthing & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
