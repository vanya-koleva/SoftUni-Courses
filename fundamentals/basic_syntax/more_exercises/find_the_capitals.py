some_string = input()
list_of_uppers = []
index = -1

for current_character in some_string:
    index += 1
    if current_character.isupper():
        list_of_uppers.append(index)

print(list_of_uppers)
