some_string = input()
final_string = ""
last_added_char = ""

for char in some_string:
    if char != last_added_char:
        final_string += char
        last_added_char = char

print(final_string)
