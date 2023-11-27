import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        # Get the file extension
        file_ext = filename.split('.')[-1]
        # Create a new directory path
        new_dir = os.path.join(directory, file_ext.upper())
        # Create a new directory if it doesn't exist
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        # Get the current file path
        file_path = os.path.join(directory, filename)
        # Get the new file path
        new_file_path = os.path.join(new_dir, filename)
        # Move the file to the new directory
        if os.path.isfile(file_path):
            shutil.move(file_path, new_file_path)

if __name__ == "__main__":
    directory = input("Enter the directory to be organized: ")
    organize_files(directory)