numbers = [int(number) for number in input().split()]
count_of_numbers_to_remove = int(input())
for number in range(count_of_numbers_to_remove):
    numbers.remove(min(numbers))
numbers = [str(number) for number in numbers]
print(", ".join(numbers))
