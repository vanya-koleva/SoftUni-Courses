length = float(input())
width = float(input())
width = width * 100 - 100
length *= 100
working_spaces_width = width // 70
working_spaces_length = length // 120
number_of_working_spaces = working_spaces_width * working_spaces_length - 3
print(int(number_of_working_spaces))
