command = input()
word = ''
c_counter = 0
o_counter = 0
n_counter = 0

while command != 'End':
    if c_counter >= 1 and o_counter >= 1 and n_counter >= 1:
        print(f'{word}', end=" ")
        word = ''
        c_counter = 0
        o_counter = 0
        n_counter = 0
    command = ord(command)
    if command in range(65, 91) or command in range(97, 123):
        command = chr(command)
        if command == 'c':
            if c_counter == 0:
                c_counter += 1
                command = input()
                continue
        elif command == 'o':
            if o_counter == 0:
                o_counter += 1
                command = input()
                continue
        elif command == 'n':
            if n_counter == 0:
                n_counter += 1
                command = input()
                continue
        word = word + command
        command = input()
    else:
        command = input()
        continue
else:
    if c_counter >= 1 and o_counter >= 1 and n_counter >= 1:
        print(f'{word}', end=" ")