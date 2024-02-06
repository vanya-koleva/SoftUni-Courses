numbers = input().split()
numbers_as_int = []

for number in numbers:
    numbers_as_int.append(int(number))

print(f"The minimum number is {min(numbers_as_int)}")
print(f"The maximum number is {max(numbers_as_int)}")
print(f"The sum number is: {sum(numbers_as_int)}")
