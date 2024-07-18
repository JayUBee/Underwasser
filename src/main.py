import numpy as np
from keras.preprocessing import image
import matplotlib.pyplot as plt
import tensorflow as tf
import os
import shutil
from utils.sequenceMapper import densest_interval	
from utils.frame_extractor import extract_frames
from utils.plot import plot_prediction


videoPath = r"C:/Users/Tayyab Butt/Desktop/thesisSupplement/video.wmv"
#extract_frames(videoPath)
image_dir = './out/'
images = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
model = tf.keras.models.load_model("./rps.h5")
graph=[]
#for fn in images:
#    # Predicting images
#    path = fn
#    filename = os.path.basename(path)
#    img = image.load_img(path, target_size=(150, 150))
#    x = image.img_to_array(img)
#    x = np.expand_dims(x, axis=0)
#
#    images = np.vstack([x])
#    classes = model.predict(images, batch_size=10)
#    print(fn)
#    print(classes)
#    if classes[0][0] == 1:
#        #remove comments to check the pictures in the folder
#        #shutil.move(path,  './out/interesting/')
#    
#        graph.append(1)
#        with open('graph.txt', 'a') as file:
#            file.write(str(filename[:(filename.__len__()) - 4]) +':'+ str(1)+'\n')
#        
#    elif classes[0][1] == 1:
#        #remove comments to check the pictures in the folder
#        #shutil.move(path, './out/not_interesting/')
#        
#        graph.append(0)
#        with open('graph.txt', 'a') as file:
#            file.write(str(filename[:(filename.__len__()) - 4]) +':'+ str(0)+'\n')

#append to file file.txt

f = graph  # Example function values
n = len(f)  # Maximum value of x
window_size = 50  # Example window size
 
densest_start, densest_end = densest_interval(f, n, window_size)
print(f"The densest interval is from x = {densest_start} to x = {densest_end}")
x_values = range(graph.__len__())

plot_prediction('graph.txt', 500)