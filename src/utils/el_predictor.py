import numpy as np
import easygui
from keras.preprocessing import image
import tensorflow as tf


imaage = easygui.fileopenbox()
model = tf.keras.models.load_model("./rps.h5")



 
 
  # predicting images
path = imaage
 # load image from path

img = image.load_img(path, target_size=(150, 150))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])
classes = model.predict(images, batch_size=10)
print(path)
print(classes)
if classes[0][0] == 1:
    print("interesting")
elif classes[0][1] == 1:
    print("not interesting")