import os

def organize_files_into_folders(directory):
    directory = os.path.abspath(directory)
    
    # Error checking for the existence of the directory
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        if os.path.isfile(item_path):
            folder_name = os.path.splitext(item)[0]
            new_folder_path = os.path.join(directory, folder_name)
            
            if not os.path.exists(new_folder_path):
                os.mkdir(new_folder_path)
            
            new_file_path = os.path.join(new_folder_path, item)
            
            # Error checking for the file move operation
            try:
                os.rename(item_path, new_file_path)
            except Exception as e:
                print(f"Error moving file {item}: {e}")

# Example usage
organize_files_into_folders(r'/mnt/data')
