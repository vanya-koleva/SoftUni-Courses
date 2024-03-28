password = input()
while True:
    command = input().split()
    if "Done" in command:
        break

    elif "TakeOdd" in command:
        password = password[1::2]

    elif "Cut" in command:
        index, length = int(command[1]), int(command[2])
        substring = password[index: index + length]
        password = password.replace(substring, "", 1)

    elif "Substitute" in command:
        substring, substitute = command[1], command[2]
        if substring in password:
            password = password.replace(substring, substitute)
        else:
            print("Nothing to replace!")
            continue

    print(password)

print(f"Your password is: {password}")
