def all_the_characters(first, second):
    for character in range(ord(first) + 1, ord(second)):
        result.append(chr(character))


first_character = input()
second_character = input()
result = []
all_the_characters(first_character, second_character)
print(" ".join(result))
