key = input()
while True:
    command = input().split(">>>")
    if "Generate" in command:
        break

    elif "Contains" in command:
        substring = command[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")

    elif "Flip" in command:
        case, start_index, end_index = command[1], command[2], command[3]
        substring = key[int(start_index): int(end_index)]
        if case == "Upper":
            key = key.replace(substring, substring.upper())
        else:
            key = key.replace(substring, substring.lower())
        print(key)

    else:
        start_index = int(command[1])
        end_index = int(command[2])
        substring = key[start_index: end_index]
        key = key.replace(substring, "")
        print(key)

print(f"Your activation key is: {key}")
