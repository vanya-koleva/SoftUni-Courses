first_char = ord(input())
second_char = ord(input())
some_string = input()
total_sum = 0

for char in some_string:
    if first_char < ord(char) < second_char:
        total_sum += ord(char)

print(total_sum)
