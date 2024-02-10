numbers = list(map(int,(input().split(", "))))
even_numbers_indices = list(map(lambda x: x if numbers[x] % 2 == 0 else "no", range(len(numbers))))
filtered_indices = list(filter(lambda x: x != "no", even_numbers_indices))
print(filtered_indices)
