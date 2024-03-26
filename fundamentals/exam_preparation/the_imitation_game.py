message = input()
while True:
    command = input().split('|')
    if "Decode" in command:
        print(f"The decrypted message is: {message}")
        break

    elif "Move" in command:
        number_of_letters = int(command[1])
        letters = message[:number_of_letters]
        message = message[number_of_letters:] + letters

    elif "Insert" in command:
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]

    else:
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)
