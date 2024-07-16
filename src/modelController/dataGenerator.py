import os
from keras_preprocessing.image import ImageDataGenerator

# Paths to your data directories
interesting_dir = os.path.join('./images/training_set/intersting/')
not_interesting_dir = os.path.join('./images/training_set/not_intersting/')

# Print total number of images in each category
print('total training interesting images:', len(os.listdir(interesting_dir)))
print('total training not interesting images:', len(os.listdir(not_interesting_dir)))

interesting_files = os.listdir(interesting_dir)
not_interesting_files = os.listdir(not_interesting_dir)



# Data augmentation for the training set
TRAINING_DIR = "./images/training_set/"
training_datagen = ImageDataGenerator(
      rescale = 1./255,
      rotation_range=40,
      width_shift_range=0.2,
      height_shift_range=0.2,
      shear_range=0.2,
      zoom_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest')

VALIDATION_DIR = "./images/validation_set/"
validation_datagen = ImageDataGenerator(rescale = 1./255)

train_generator = training_datagen.flow_from_directory(
    TRAINING_DIR,
    target_size=(150, 150),
    class_mode='categorical',  # Use 'categorical' for multi-class classification
    batch_size=36
)

validation_generator = validation_datagen.flow_from_directory(
    VALIDATION_DIR,
    target_size=(150, 150),
    class_mode='categorical',  # Use 'categorical' for multi-class classification
    batch_size=126
)
