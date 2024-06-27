import os

while True:
    command, *info = input().split("-")

    if command == "End":
        break

    path = os.path.join("text_files", f"{info[0]}")

    if command == "Create":
        with open(path, "w"): pass

    elif command == "Add":
        with open(path, "a") as file:
            file.write(f"{info[1]}\n")

    elif command == "Replace":
        try:
            with open(path, "r+") as file:
                text = file.read()
                text = text.replace(info[1], info[2])

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(path)
        except FileNotFoundError:
            print("An error occurred")
