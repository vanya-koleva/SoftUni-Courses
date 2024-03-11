list_of_strings = input().split()
total_sum = 0

for current_string in list_of_strings:
    first_letter = current_string[0]
    last_letter = current_string[-1]
    number = int(current_string[1:-1])

    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        total_sum += number / first_letter_position
    else:
        first_letter_position = ord(first_letter) - 96
        total_sum += number * first_letter_position

    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_sum -= last_letter_position
    else:
        last_letter_position = ord(last_letter) - 96
        total_sum += last_letter_position

print(f"{total_sum:.2f}")
