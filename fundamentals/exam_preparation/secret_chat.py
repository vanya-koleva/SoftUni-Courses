message = input()
while True:
    command = input().split(":|:")
    if "Reveal" in command:
        break

    elif "InsertSpace" in command:
        index = int(command[1])
        message = message[:index] + " " + message[index:]

    elif "Reverse" in command:
        substring = command[1]
        if substring not in message:
            print("error")
            continue
        else:
            message = message.replace(substring, "", 1)
            message += substring[::-1]

    elif "ChangeAll" in command:
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

    print(message)

print(f"You have a new text message: {message}")
