#code to extract all videos from the WSASL100 structued dataset folder and save them in a single folder
import os
import shutil

# Specify the folder containing subfolders with videos
input_folder = '/Users/mariewesthues/Library/Mobile Documents/com~apple~CloudDocs/Universität/Master/Köln/WS24:25/Advanced Data Analytics for Business /ADA - Project/code/WLASL100'
# Specify the output folder where all videos will be saved
output_folder = '/Users/mariewesthues/Library/Mobile Documents/com~apple~CloudDocs/Universität/Master/Köln/WS24:25/Advanced Data Analytics for Business /ADA - Project/code/WSASL100_single'
os.makedirs(output_folder, exist_ok=True)

# Supported video file extensions (modify as needed)
video_extensions = ('.mp4', '.avi', '.mov', '.mkv')  

# Walk through the input folder
for root, dirs, files in os.walk(input_folder):
    for file in files:
        # Check if the file is a video
        if file.endswith(video_extensions):
            source_path = os.path.join(root, file)
            target_path = os.path.join(output_folder, file)
            
            # If a file with the same name exists in the output folder, rename to avoid overwriting
            if os.path.exists(target_path):
                base, ext = os.path.splitext(file)
                target_path = os.path.join(output_folder, f"{base}_copy{ext}")
            
            # Copy the video to the output folder
            shutil.copy(source_path, target_path)
            print(f"Copied {source_path} to {target_path}")

print(f"All videos have been extracted to {output_folder}.")
