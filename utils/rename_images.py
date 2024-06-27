import os
import glob

# Define the path of the folder
folder_path = './data/'

filenames=glob.glob(folder_path+"**.*g")
print(len(filenames))

for index, file in enumerate(filenames):
    current_name = file.split("/")[-1]
    ext = current_name.split(".")[-1]
    new_name = f"{index}.{ext}"
    
    current_path = os.path.join(folder_path, current_name)
    new_path = os.path.join(folder_path, new_name)
    os.rename(current_path, new_path)
