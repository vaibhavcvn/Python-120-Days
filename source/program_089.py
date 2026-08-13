import os

file_name = "sample.txt"

if os.path.exists(file_name):
    print("File exists.")
    print("File size:", os.path.getsize(file_name), "bytes")
else:
    print("File does not exist.")
