import os

folder = "test_folder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder created.")
else:
    print("Folder already exists.")
