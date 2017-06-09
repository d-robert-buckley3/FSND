import os
from string import digits

def rename_files():
    # create list of filenames in folder
    file_list = os.listdir(r"C:\Users\cardi\Downloads\prank\prank")
    #print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\cardi\Downloads\prank\prank")
    
    # for each file, remove numeric chars from filename
    for file_name in file_list:
        new_file_name = file_name.translate(None, digits)
        print("Changing: " + file_name + "-->" + new_file_name)
        os.rename(file_name, new_file_name)

    os.chdir(saved_path)

rename_files()
