numbers = [int(x) for x in input().split()]
average = sum(numbers) / len(numbers)
above_average_numbers = [x for x in numbers if x > average]
above_average_numbers = sorted(above_average_numbers, reverse=True)
if above_average_numbers:
    print(*above_average_numbers[:5])
else:
    print("No")
