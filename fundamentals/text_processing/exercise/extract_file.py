file_path = input().split("\\")
file = file_path[-1].split(".")
file_name, file_extension = file
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
