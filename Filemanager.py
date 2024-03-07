import os
import shutil
path = input("Enter your path: ")
files = os.listdir(path)
for i in files:
    filename, extension = os.path.splitext(i)
    extension_1 = extension[1:]
    folder_path = path + "\\" + extension_1
    if os.path.exists(folder_path):
        shutil.move(path+"\\"+i, path+"\\"+extension_1+"\\"+i)
        #1st path where your file is
        #2nd path where it is tranfered
    else:
        os.makedirs(folder_path)
        shutil.move(path+"\\"+i, path+"\\"+extension_1+"\\"+i)

    print(extension_1)