num = int(input())
word = input()
all_strings = []
filtered_list = []

for i in range(num):
    current_string = input()
    all_strings.append(current_string)

for element in range(len(all_strings)):
    if word in all_strings[element]:
        filtered_list.append(all_strings[element])

print(all_strings)
print(filtered_list)
