import os

path = os.path.join("..", "03_file_writer", "my_first_file.txt")

if os.path.exists(path):
    os.remove(path)
else:
    print("File does not exist")
