single_string = input()
final_message = ""
repetitions = ""
sub_string = ""

for index in range(len(single_string)):
    if not single_string[index].isdigit():
        sub_string += single_string[index].upper()
    else:
        for next_symbols in range(index, len(single_string)):
            if not single_string[next_symbols].isdigit():
                break
            repetitions += single_string[next_symbols]
        final_message += sub_string * int(repetitions)
        repetitions = ""
        sub_string = ""

print(f"Unique symbols used: {len(set(final_message))}")
print(final_message)
