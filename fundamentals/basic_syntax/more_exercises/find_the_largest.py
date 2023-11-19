number = list(input())
number.sort(reverse=True)
largest = ''
for digit in number:
    largest += digit
print(largest)
