import cv2 as CV
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing import image

#This is a copy from Binary Classification...
image_size = 128
classifier = Sequential() # Our network is Sequential...
classifier.add(Conv2D(image_size//4, (3, 3), #32 is the numberof filters (?), the (3,3) is shape of filter
                      input_shape = (image_size, image_size, 3), 
                      activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))#Maybe see if we can do without pooling as I don't understand it
#Although the cite says pooling reduces computation time so whatever
classifier.add(Flatten())
classifier.add(Dense(units = 128, activation = 'relu')) #Dense adds a second layer
classifier.add(Dense(units = 32, activation = 'relu')) #Dense adds a second layer
classifier.add(Dense(units = 1, activation = 'sigmoid'))#This last one is a sigmoid, its the output. Ether 0 (Nodab) or 1(dab). Although likely somewhere inbetween
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
#That copy ends here
classifier.load_weights("Classy.h5")

i = 0

Filename = "NewImages/std_img"
Output_Directory = "Default_Output"
while(i < 4159):
    tempfilename = Filename + str(i) + ".jpg"
    CVFILE = CV.imread(tempfilename)
    if (CVFILE is None):
        print("File not found:", tempfilename)
        exit()
    #temp_image = CV.cvtColor(CVFILE, CV.COLOR_BGR2GRAY)#temp_image is the image after removing color, for the purposes of edge detection
    #temp_image = CV.medianBlur(temp_image, 7)#also remove temp's garbage by adding blur
    #Edges = CV.Laplacian(temp_image, CV.CV_8U, 5)#default was 5 I have no idea
    CV.imwrite("Temp.jpg", CVFILE)
    test_image = image.load_img("Temp.jpg", target_size = (image_size, image_size))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict(test_image)
    if (result[0][0] == 1):
        CV.imwrite(Output_Directory + "/Std/std_img" + str(i) + ".jpg", CVFILE)
    else:
        CV.imwrite(Output_Directory + "/Pose/pose_img" + str(i) + ".jpg", CVFILE)
    i = i + 1
print("Donski")