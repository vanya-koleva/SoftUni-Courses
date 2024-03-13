def extract_name_and_age(text: str):
    name = ""
    age = ""
    for index in range(len(text)):
        if text[index] == "@":
            for next_symbols in range(index +1, len(text)):
                if text[next_symbols] == "|":
                    break
                name += text[next_symbols]

        elif text[index] == "#":
            for next_symbols in range(index + 1, len(text)):
                if text[next_symbols] == "*":
                    break
                age += text[next_symbols]

    return f"{name} is {age} years old."


number_of_lines = int(input())
for i in range(number_of_lines):
    line = input()
    print(extract_name_and_age(line))
