numbers_as_str = input().split()
some_string = input()

indices = []
message = ""

# Find the indices by summing the digits of the numbers
for number in numbers_as_str:
    sum_of_digits = 0
    for digit in number:
        sum_of_digits += int(digit)
    indices.append(sum_of_digits)

# Make the indices valid, then append the corresponding character to the message
# and remove it from the string
for index in indices:
    index %= len(some_string)
    char = some_string[index]
    message += char
    some_string = some_string.replace(char, "", 1)

print(message)
