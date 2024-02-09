numbers_as_string = input().split(", ")
numbers_as_integers = [int(number) for number in numbers_as_string]
# zeroes = []
#
# Move all zeroes from one list to another
# while 0 in numbers_as_integers:
#     numbers_as_integers.remove(0)
#     zeroes.append(0)
#
# Append zeroes to the end
# final_result = numbers_as_integers + zeroes
# print(final_result)

# Count the number of zeroes
zeroes_count = numbers_as_integers.count(0)

# Remove all zeroes
numbers_as_integers = [number for number in numbers_as_integers if number != 0]

# Append zeroes to the end
final_result = numbers_as_integers + [0]*zeroes_count

print(final_result)
