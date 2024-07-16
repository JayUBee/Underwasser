import cv2
import os

# Path to the video file
video_path = "./video.wmv"

    

# Create a directory to store the extracted frames
output_dir = "./out"
os.makedirs(output_dir, exist_ok=True)

# Open the video file
video = cv2.VideoCapture(video_path)


# Initialize frame counter
frame_count = 0
i=0
frame_per_frames = 300
# Read frames from the video
while True:
    # Read the next frame
    ret, frame = video.read()

    # Break the loop if no more frames are available
    if not ret:
        break
    # Save the frame as an image
    if(frame_count%frame_per_frames == 0 ) :
        output_path = os.path.join(output_dir, f"img{i}.jpg")
        cv2.imwrite(output_path, frame)
        i += 1

    # Increment the frame counter
    frame_count += 1
    

# Release the video file
video.release()