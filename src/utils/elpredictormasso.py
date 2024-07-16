import numpy as np
from keras.preprocessing import image
import tensorflow as tf
import os
import shutil

image_dir = './out/'
images = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
model = tf.keras.models.load_model("./rps.h5")
i = 0
for fn in images:
    # Predicting images
    path = fn
    img = image.load_img(path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    print(fn)
    print(classes)
    if classes[0][0] == 1:
        print("interesting")
        shutil.move(path,  './dout/interesting/')
        i += 1

    elif classes[0][1] == 1:
        print("not interesting")
        shutil.move(path, './dout/not_interesting/')
        i += 1