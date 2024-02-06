list_of_numbers = input().split()

list_of_absolute_values = [abs(float(number)) for number in list_of_numbers]

print(list_of_absolute_values)