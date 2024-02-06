def has_errors(some_string):
    errors = []
    if not 6 <= len(some_string) <= 10:
        errors.append("Password must be between 6 and 10 characters")
    if not some_string.isalnum():
        errors.append("Password must consist only of letters and digits")
    digits = 0
    for character in some_string:
        if character.isdigit():
            digits += 1
    if digits < 2:
        errors.append("Password must have at least 2 digits")
    return errors


password = input()
if not has_errors(password):
    print("Password is valid")
else:
    print("\n".join(has_errors(password)))
