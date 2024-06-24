import os

try:
    path = os.path.join("text.txt")
    file = open(path)
    print("File found")
    file.close()
except FileNotFoundError:
    print("File not found")
