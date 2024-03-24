def process_valid(name: str, command_: list) -> None:
    char = command_[1]
    if char in name:
        print("Valid username.")
    else:
        print(f"{char} must be contained in your username.")


def process_replace(name: str, command_: list) -> str:
    char = command_[1]
    if char in name:
        name = name.replace(char, "-")
        print(name)
    return name


def process_substring(name: str, command_: list) -> str:
    searched_substring = command_[1]
    if searched_substring in name:
        name = name.replace(searched_substring, "")
        print(name)
    else:
        print(f"The username {name} doesn't contain {searched_substring}.")
    return name


def process_reverse(name: str, command_: list) -> None:
    start_index, end_index = int(command_[1]), int(command_[2])
    if 0 <= start_index < len(name) and 0 <= end_index < len(name):
        new_string = name[start_index: end_index + 1]
        print(new_string[::-1])


def process_letters(name: str,command_: list) -> str:
    if "Lower" in command_:
        name = name.lower()
    elif "Upper" in command_:
        name = name.upper()
    print(name)
    return name


username = input()

while True:
    command = input().split()
    if "Registration" in command:
        break

    if "Letters" in command:
        username = process_letters(username,command)

    elif "Reverse" in command:
        process_reverse(username, command)

    elif "Substring" in command:
        username = process_substring(username, command)

    elif "Replace" in command:
        username = process_replace(username, command)

    elif "IsValid" in command:
        process_valid(username, command)
