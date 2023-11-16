number_of_pairs = int(input())
max_difference = 0
first_number = int(input())
second_number = int(input())
value = first_number + second_number

for i in range(number_of_pairs - 1):
    current_first_number = int(input())
    current_second_number = int(input())
    current_value = current_first_number + current_second_number
    difference = abs(value - current_value)
    if difference > max_difference:
        max_difference = difference
    value = current_value

if max_difference != 0:
    print(f"No, maxdiff={max_difference}")
else:
    print(f"Yes, value={value}")
