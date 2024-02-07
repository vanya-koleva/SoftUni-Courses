key = int(input())
number_of_characters = int(input())
message = ""

for current_character in range(number_of_characters):
    character = input()
    letter = ord(character) + key
    message += chr(letter)

print(message)
