starting_number = int(input())
final_number = int(input())

for current_number in range(starting_number, final_number + 1):
    current_number_as_string = str(current_number)
    even_digits_sum = 0
    odd_digits_sum = 0
    for position, digit in enumerate(current_number_as_string):
        if position % 2 == 0:
            odd_digits_sum += int(digit)
        else:
            even_digits_sum += int(digit)
    if even_digits_sum == odd_digits_sum:
        print(current_number, end= " ")