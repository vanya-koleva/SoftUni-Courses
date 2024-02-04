number_of_lines = int(input())
total_sum = 0

for _ in range(number_of_lines):
    letter = input()
    number = ord(letter)
    total_sum += number

print(f"The sum equals: {total_sum}")