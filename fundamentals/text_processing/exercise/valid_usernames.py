def check_redundant(name):
    if " " in name:
        return False
    return True


def check_characters(name):
    for character in name:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def check_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def username_is_validated(name):
    if check_length(name) and check_characters(name) and check_redundant(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_validated(username):
        print(username)
