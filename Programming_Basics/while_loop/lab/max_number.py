max_number = int(input())

while True:
    user_input = input()
    if user_input == 'Stop':
        break
    user_input = int(user_input)
    if max_number < user_input:
        max_number = user_input

print(max_number)