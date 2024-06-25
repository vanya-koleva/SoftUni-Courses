n = int(input())


def print_upper_part(size):
    for row in range(1, size + 1):
        print(f"{' ' * (size - row)}{'* ' * row}")


def print_bottom_part(size):
    for row in range(size - 1, 0, -1):
        print(f"{' ' * (size - row)}{'* ' * row}")


print_upper_part(n)
print_bottom_part(n)
