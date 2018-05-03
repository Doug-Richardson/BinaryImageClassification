from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
print("Start...")
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
#adam is stochastic gradiant decent
#loss is type of loss function
#Metrics is to disply performance metrics.

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)
training_set = train_datagen.flow_from_directory('Test',#Name of directory
                                                 target_size = (image_size, image_size),#Size the images will be rescaled to
                                                 batch_size = 32,#idk
                                                 class_mode = 'binary')#lol

test_set = test_datagen.flow_from_directory('Validate',
                                            target_size = (image_size, image_size),
                                            batch_size = 32,
                                            class_mode = 'binary')


classifier.fit_generator(training_set,
                         steps_per_epoch = 500,#Number of images in traningset. I don't think thats true... After 500 its about as good as it gets
                         epochs = 5,#Was 25 as default, I don't know if it matters.
                         validation_data = test_set,#This ain't right
                         validation_steps = 160)#Number of images in validation set.
classifier.save("Classy_bw.h5")#yay?
print("We done!")