start_number = int(input())
final_number = int(input())

for current_number in range(start_number, final_number + 1):
    odd_numbers_sum = 0
    even_numbers_sum = 0
    current_number_as_string = str(current_number)
    for index in range(len(current_number_as_string)):
        for index, digit in enumerate(current_number_as_string):
            if index % 2 == 0:
                odd_numbers_sum += int(digit)
            else:
                even_numbers_sum += int(digit)
    if odd_numbers_sum == even_numbers_sum:
        print(current_number, end=" ")