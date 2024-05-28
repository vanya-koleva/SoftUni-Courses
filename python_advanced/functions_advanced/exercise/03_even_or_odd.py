def even_odd(*args):
    command = args[-1]

    if command == "even":
        result = [x for x in args[:-1] if not x % 2]
    else:
        result = [x for x in args[:-1] if x % 2]

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
