import cv2
import os
import math

# Path to the video file
def extract_frames(video_path):
   
    # Create a directory to store the extracted frames
    output_dir = "./out"
    os.makedirs(output_dir, exist_ok=True)

    # Open the video file
    video = cv2.VideoCapture(video_path)

    fps = video.get(cv2.CAP_PROP_FPS)
    totalNoFrames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    durationInSeconds = totalNoFrames // fps

    # Initialize frame counter
    frame_count = 0
    i=0
    frame_per_frames = 100
    # Read frames from the video
    while True:
        # Read the next frame
        ret, frame = video.read()
        timestamp = video.get(cv2.CAP_PROP_POS_MSEC)/1000
        # Break the loop if no more frames are available
        if not ret:
            break
        # Save the frame as an image
        if(frame_count%frame_per_frames == 0 ) :
            timestamp = video.get(cv2.CAP_PROP_POS_MSEC)/1000
            percentage = (timestamp/durationInSeconds)*100  
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"extracting frames ... \n progress:{math.floor(percentage)}%")
            output_path = os.path.join(output_dir, f"{math.floor(timestamp)}.jpg")
            cv2.imwrite(output_path, frame)
            i += 1

        # Increment the frame counter
        frame_count += 1


    # Release the video file
    video.release()