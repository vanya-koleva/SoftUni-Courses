starting_number = int(input())
final_number = int(input())
magic_number = int(input())
combinations_counter = 0
combination_is_found = False

for first_number in range(starting_number, final_number + 1):
    for second_number in range(starting_number, final_number + 1):
        combinations_counter += 1
        if first_number + second_number == magic_number:
            combination_is_found = True
            break
    if combination_is_found:
        break

if combination_is_found:
    print(f"Combination N:{combinations_counter} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combinations_counter} combinations - neither equals {magic_number}")