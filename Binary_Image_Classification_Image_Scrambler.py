#IF YOU ARE LOOKING FOR A REAL FILE, YOU IN THE WRONG PLACE BROTHER
import numpy as np
import cv2
from random import randint as rand
filename = ""
Validation_Size = 1
Max_size = 10 #So random(1,max_size) if less than or equal to validation size, then its part of validation set...
input_pose = "Input\Pose\pose_img"#Damn
input_std = "Input\Std\std_img"
output_pose = "Pose\pose_img"
output_std = "Std\std_img"
Validationset = "Output\Validate\\"
Testset = "Output\Test\\"
#First the std files
end = False
i = 0
k = 473
while(not end):
    i = i + 1
    k = k + 1
    #try:
    filename = input_std + str(i) + ".jpg"
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    if (image is None):
        print("Std i =", i)
        end = True
    output = ""
    if (rand(1,Max_size) <= Validation_Size):
        output = Validationset
    else:
        output = Testset
    output = output + output_std + str(k) + ".jpg"
    cv2.imwrite(output, image)
end = True
i = 0
k = 300
while(not end):
    i = i + 1
    k = k + 1
    #try:
    filename = input_pose + str(i) + ".jpg"
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    if (image is None):
        print("Pose i =", i)
        end = True
    output = ""
    if (rand(1,Max_size) <= Validation_Size):
        output = Validationset
    else:
        output = Testset
    output = output + output_pose + str(k) + ".jpg"
    cv2.imwrite(output, image)

print("Donski!")

