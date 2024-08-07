import numpy as np
from keras.preprocessing import image
import tensorflow as tf
import os
from utils.frame_extractor import extract_frames
from utils.plot import plot_prediction
import math
import shutil


videoPath = r"C:/Users/Ismail/Desktop/supplement/video.wmv"
#extract_frames(videoPath)
image_dir = './out/'
images = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
num_images = len(images)
model = tf.keras.models.load_model("./rps.h5")
graph=[]
i=0
percent = 0 
for fn in images:
    # Predicting images
    path = fn
    filename = os.path.basename(path)
    img = image.load_img(path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10, verbose=0)
    if classes[0][0] == 1:
        #toggle comments to move the pictures in the folder
        #shutil.move(path,  './out/interesting/')
    
        graph.append(1)
        i+=1
        percent =  math.floor((i/num_images)*100)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"classifying images... \nprogress:{percent}%")
        with open('graph.txt', 'a') as file:
            file.write(str(filename[:(filename.__len__()) - 4]) +':'+ str(1)+'\n')
        
    elif classes[0][1] == 1:
        #toggle comments to move the pictures in the folder
        #shutil.move(path, './out/not_interesting/')
        
        graph.append(0)
        i+=1
        percent = math.floor((i/num_images)*100)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"classifying images... \nprogress:{percent}%")
        with open('graph.txt', 'a') as file:
            file.write(str(filename[:(filename.__len__()) - 4]) +':'+ str(0)+'\n')




plot_prediction('graph.txt')