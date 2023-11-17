while True:
    command = input()
    if command == "End":
        break
    elif command == "SoftUni":
        continue
    for i in range(len(command)):
        letter = command[i]
        print(letter * 2, end="")
    print()