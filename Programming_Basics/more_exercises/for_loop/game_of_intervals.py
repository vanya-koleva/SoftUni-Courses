number_of_moves = int(input())
from_0_to_9_counter = 0
from_10_to_19_counter = 0
from_20_to_29_counter = 0
from_30_to_39_counter = 0
from_40_to_50_counter = 0
invalid_counter = 0
result = 0
total_numbers = 0

for i in range(number_of_moves):
    current_number = int(input())
    total_numbers += 1
    if 0 <= current_number <= 9:
        from_0_to_9_counter += 1
        result += current_number * 0.2
    elif 10 <= current_number <= 19:
        from_10_to_19_counter += 1
        result += current_number * 0.3
    elif 20 <= current_number <= 29:
        from_20_to_29_counter += 1
        result += current_number * 0.4
    elif 30 <= current_number <= 39:
        from_30_to_39_counter += 1
        result += 50
    elif 40 <= current_number <= 50:
        from_40_to_50_counter += 1
        result += 100
    else:
        invalid_counter += 1
        result /= 2

from_0_to_9_percentage = from_0_to_9_counter / total_numbers * 100
from_10_to_19_percentage = from_10_to_19_counter / total_numbers * 100
from_20_to_29_percentage = from_20_to_29_counter / total_numbers * 100
from_30_to_39_percentage = from_30_to_39_counter / total_numbers * 100
from_40_to_50_percentage = from_40_to_50_counter / total_numbers * 100
invalid_percentage = invalid_counter / total_numbers * 100

print(f'{result:.2f}')
print(f"From 0 to 9: {from_0_to_9_percentage:.2f}%")
print(f"From 10 to 19: {from_10_to_19_percentage:.2f}%")
print(f"From 20 to 29: {from_20_to_29_percentage:.2f}%")
print(f"From 30 to 39: {from_30_to_39_percentage:.2f}%")
print(f"From 40 to 50: {from_40_to_50_percentage:.2f}%")
print(f"Invalid numbers: {invalid_percentage:.2f}%")