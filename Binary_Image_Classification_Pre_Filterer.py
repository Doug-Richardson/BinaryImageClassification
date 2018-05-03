import cv2 as CV
import numpy as num
i = 0
k = 0
Category = "Test/Validate"
imagetype = "std/pose"
foldername = "Std/Pose"
max_count = -1
while (k <= 3):
    if (k % 2 == 0):
        imagetype = "std"
        foldername = "Std"
        max_count = 473
    else:
        imagetype = "pose"
        foldername = "Pose"
        max_count = 300
    if (k > 1):
        Category = "Validate"
    else:
        Category = "Test"
    i = 0
    while(i < max_count):
        i = i + 1
        Filename = Category + "\\" + foldername + "\\" + imagetype + "_img" + str(i) + ".jpg"
        Input_Filename = "Input\\" + Filename  
        image = CV.imread(Input_Filename,CV.IMREAD_COLOR)
        if (image is None):
            print("Image", imagetype, i, "Not found in folder", Category)
        else:
            temp_image = CV.cvtColor(image, CV.COLOR_BGR2GRAY)#temp_image is the image after removing color, for the purposes of edge detection
            temp_image = CV.medianBlur(temp_image, 7)#also remove temp's garbage by adding blur
            Edges = CV.Laplacian(temp_image, CV.CV_8U, 5)#default was 5 I have no idea
            Output_Filename = "Output\\" + Filename
            CV.imwrite(Output_Filename, Edges)
    k = k + 1