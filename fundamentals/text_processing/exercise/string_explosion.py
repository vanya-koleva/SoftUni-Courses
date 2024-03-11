some_string = input()
final_string = ""
explosion = 0

for index in range(len(some_string)):
    if explosion > 0 and some_string[index] != '>':
        explosion -= 1
    elif some_string[index] == '>':
        final_string += '>'
        explosion += int(some_string[index + 1])
    else:
        final_string += some_string[index]

print(final_string)
