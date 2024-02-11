first_sequence = input().split(", ")
second_sequence = input()
substrings = [x for x in first_sequence if x in second_sequence]
print(substrings)
