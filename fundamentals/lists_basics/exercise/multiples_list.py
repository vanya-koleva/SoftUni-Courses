factor = int(input())
count = int(input())
list_with_numbers = []
for number in range(1, count + 1):
    list_with_numbers.append(number * factor)
print(list_with_numbers)
