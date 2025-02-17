import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[-1].lower()
            destination_folder = os.path.join(directory, file_extension[1:].upper())
            os.makedirs(destination_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(destination_folder, file))
    
    print("Files organized successfully!")

if __name__ == "__main__":
    folder_to_organize = input("Enter the folder path to organize: ")
    organize_files(folder_to_organize)