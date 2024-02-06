numbers = input().split()
numbers_as_digits = []
for number in numbers:
    numbers_as_digits.append(int(number))

is_even = lambda x: x % 2 == 0
even_numbers = list(filter(is_even, numbers_as_digits))
print(even_numbers)
