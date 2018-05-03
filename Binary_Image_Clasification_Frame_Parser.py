import numpy as np
import cv2
filename = 'Video_CV_Project_3\MOVI00'
num = -1
num_as_str = '00'#00 does not exist, it starts at 1
filetype = '.avi'
Posecount = 0
Stdcount = 0
while (num < 1):
    num = num + 1
    print("#", num)
    if (num < 10):
        num_as_str = '0' + str(num)
    else:
        num_as_str = str(num)
    cap = cv2.VideoCapture(filename+num_as_str+filetype)
    framecount = 0
    while (cap.isOpened()):
        framecount = framecount + 1
        if (framecount % 100 == 0):
            print(framecount)
        ret, frame = cap.read()
        if (frame is None):
            break
        #Save to relevant place
        is_pose = False
        #The below varies from different viedo files

        #The above varies from project to project
        if(is_pose):
            tmp = "Pose\pose_img"
            tmp = tmp + str(Posecount) + ".jpg"
            cv2.imwrite(tmp, frame)
            Posecount = Posecount + 1
        else:
            if (framecount % 2 == 0):#Every frame is too often, so do every 100 frames.
                tmp = "Std\std_img"
                tmp = tmp + str(Stdcount) + ".jpg"
                cv2.imwrite(tmp, frame)
                Stdcount = Stdcount + 1
print("Done!")
