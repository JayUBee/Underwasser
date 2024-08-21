import cv2
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from skimage.feature import graycomatrix, graycoprops
from utils.frame_extractor import extract_frames
import math

# Directory containing the images
videoPath = r"C:/Users/Ismail/Desktop/supplement/video.wmv"
extract_frames(videoPath)
image_dir = 'out/'

# Function to calculate texture features and return a combined texture index
def calculate_texture_index(image):
    glcm = graycomatrix(image, distances=[5], angles=[0], symmetric=True, normed=True)
    contrast = graycoprops(glcm, 'contrast')[0, 0]
    dissimilarity = graycoprops(glcm, 'dissimilarity')[0, 0]
    homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]
    energy = graycoprops(glcm, 'energy')[0, 0]
    correlation = graycoprops(glcm, 'correlation')[0, 0]
    asm = graycoprops(glcm, 'ASM')[0, 0]
    texture_index = contrast + dissimilarity + homogeneity + energy + correlation + asm
    return texture_index

# Initialize lists to store timestamps and texture indices
timestamps = []
texture_indices = []
images= [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
num_images = len(images)
i=0

# Loop through all files in the directory
for filename in os.listdir(image_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        image_path = os.path.join(image_dir, filename)
        timestamp = filename.split('.')[0]
        print(timestamp)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        texture_index = calculate_texture_index(image)
        timestamps.append(int(timestamp))
        texture_indices.append(texture_index)
        i+=1
        percent =  math.floor((i/num_images)*100)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"analysing image texture... \nprogress:{percent}%")

# Convert timestamps to a sorted list
timestamps, texture_indices = zip(*sorted(zip(timestamps, texture_indices)))

# Convert timestamps to integers for better handling

# Plot the texture index over time
plt.figure(figsize=(15, 6))  # Increase figure size

plt.plot(timestamps, texture_indices, marker='o')
plt.xlabel('Timestamp Index')
plt.ylabel('Texture Index')
plt.title('Texture Index Over Time')

# Reduce the number of x-axis ticks
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=10))  # Adjust nbin as needed

# Rotate and format x-axis labels


plt.tight_layout()  # Automatically adjust subplot parameters to give specified padding
plt.show()
