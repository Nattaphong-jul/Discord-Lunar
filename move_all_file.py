import os
import shutil

def move_all_files(src_dir, dest_dir):
    # Ensure the destination directory exists, create if it doesn't
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate over all files in the source directory
    for filename in os.listdir(src_dir):
        src_path = os.path.join(src_dir, filename)
        dest_path = os.path.join(dest_dir, filename)

        # Check if it's a file before moving (ignoring subdirectories)
        if os.path.isfile(src_path):
            shutil.move(src_path, dest_path)
            print(f"Moved {filename} to {dest_dir}")