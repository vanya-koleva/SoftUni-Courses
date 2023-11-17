divisor = int(input())
boundary = int(input())
largest = 0

for current_number in range(boundary, divisor - 1, -1):
    if current_number % divisor == 0:
        largest = current_number
        break

print(largest)