list_with_numbers = input().split()
new_list_with_numbers = []
for number in list_with_numbers:
    number = -int(number)
    new_list_with_numbers.append(number)
print(new_list_with_numbers)