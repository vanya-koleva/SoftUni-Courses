def data_types(command, string):
    if command == "string":
        return f"${string}$"

    elif command == "int":
        number = int(string)
        return number * 2

    else:
        number = float(string)
        number *= 1.5
        return f"{number:.02f}"


command_ = input()
string_ = input()
print(data_types(command_, string_))
