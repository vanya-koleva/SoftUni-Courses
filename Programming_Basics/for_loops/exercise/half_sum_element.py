import math

count_of_numbers = int(input())
max_element = -math.inf
total_sum = 0

for number in range(count_of_numbers):
    current_number = int(input())
    if current_number > max_element:
        max_element = current_number
    total_sum += current_number
total_sum -= max_element
difference = abs(total_sum - max_element)
if max_element == total_sum:
    print('Yes')
    print(f'Sum = {max_element}')
else:
    print('No')
    print(f'Diff = {difference}')