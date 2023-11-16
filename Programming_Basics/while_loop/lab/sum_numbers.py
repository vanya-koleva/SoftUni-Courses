number = int(input())
sum = 0

while True:
    current_number = int(input())
    sum += current_number
    if sum >= number:
        break
print(sum)