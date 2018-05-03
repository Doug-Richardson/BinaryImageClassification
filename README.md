# BinaryImageClassification
Computer vision project to create a binary image classification program that specifically uses a small, self made dataset.

Read the CV paper for more information on why this exists and how it works. The below section exists to explain the functionality of each program as well as intended use.

# FOR INTENDED USE
This program was never intended to be more than a proof of concept. The code itself has many issues that I would not leave if it was a product I had intended others to use for actual use. If you plan on using this code, be warned that it was specially designed around the filesystem I had been using and WILL require you to alter many lines of code to get working with your own dataset. User discression is advised, as is basic understanding of python programing.

The best information on how all of the things I use in the programs actually work can be found in the CV Paper as well as the refrences of that paper.

# Binary_Image_Classification
This is the important program. It is able to create a neural network that identifies a pose from a set of images. A description from the paper is below.

It starts by defining classifier as a Sequential from kreas.models. This refers to the type of method it uses internally to represent the network. Next we add 2d convocation to that network. The shape of the convocation changed often through development as I tinkered with the neural network. I flatten the classifier and add several different layers, most importantly ending with a sigmoid with a single unit to make the network output only a 0 or a 1 to determine if it is detecting the pose or not. I compile the classifier with the adam optimizer which is a stochastic gradient descent, meaning as new data points are added it optimizes based on the gradient of changes. The loss function is binary cross entropy, something I truthfully don’t understand too well, however showed the best results. I also have it display accuracy by adding it as a metric.
The image generators in the next part of the code are there to create even more images from the limited dataset available. They will flip, rotate, scale, and blur the images and add them as additional data points. After all is said and done, I fit the neuralnetwork to the set. I use 5 epochs because each epoch takes a long time to complete, but one is not reliable enough. Afterwords I save the classifier as a .h5 so I can re-use it later without needing to compile everything again. It is important to note this only saves the weights, which is why in the final test program there is some code taken directly from this program that is largely unchanged. They create the same neural network, it just needs to load the weights for each node.

Before running the program ensure that the directories named "Validate" and "Test" are in the same directory as the program. Results may varry. The output is a set of weights representing the neural network known as "Classy.h5"

# Binary_Image_Classification_Frame_Parser
This program exists to parse the frames from a set of video files into two categories, "Pose" and "Std" which stands for standard. I kept the files in a directory called "Video_CV_Project_3" and each file was named something allong the lines of "MOVI00" followed by a 2 digit number. Change these if that doesn't match your setup. Be advised that it will continue to attempt to read MOVI00## files until it has reached the number specified by condition of the first while loop (num < 1).

One last important thing to note is the presence of the comments that say "The below/above varies from different viedo files". If you intend to use this, here is where you would specify when the pose is identified. For example if the 44th frame is identified as a pose from the 2nd video, you could use the following statement
if(num == 2):
  if(framecount == 44):
    is_pose = True
This will seperate frames that change the is_pose flag from those that do not.

# Binary_Image_Classification_Image_Scrambler
This program exists to create a validation and test set out of a large parsed set of images. It will randomly select 10% of images to be a part of the validation set and the rest part of the test set. It requires a directory called "Input" with sub directories "Pose" and "Std" and lastly images with the named "pose_img#.jpg" and "std_img#.jpg" where # is the enumeration of the image in it's smallest written form (so it would be 1, not 01 or 001). It also requires an "Output" directory with "Test" and "Validation" subdirectories in that and to each of those their own "Std" and "Pose" directories in that.

# Binary_Image_Classification_Pre_Filterer
Takes a "Test" and "Validate" set and applies a filter onto it. As with previous programs, it requires an "Output" directory with coresponding "Test", "Validate" and "Pose"/"Std" subdirectories in each. The output of the Image Scrambler may act as input for this, as long as it is in the "Input" Directory. After the final if statement in the code is where the filters are applied, so if you want to specify a different filter, just change what is after the else block and be sure to write the changes to the proper place.

# Binary_Image_Classification_Video_Viewer
Once again I kept the files in a directory called "Video_CV_Project_3" and each file was named something allong the lines of "MOVI00" followed by a 2 digit number. This program is designed to assist in locating the exact frames a pose exists within. Pressing the spacebar will cause the video to pause. While paused pressing the 'o' key rewinds 100 frames and using the 'l' key advances 1 frame. Holding the 'l' key advances 1 frame slower than un-paused. The current frame number is displayed in stdout, the number after that (a negitave number) is the number of frames before the most recently shown frame, and can for the most part be ignored.

# Binary_Classification_Final_Test
This was used to test a neural network against a host of new images. It loads the weight from a file called "Classy.h5" and sorts the images into two directories called "Pose" and "Std". In the version currently on this github, it will also send the image through a filter. This was the filter that my last neural network was trained with and was not included in other neural networks.
