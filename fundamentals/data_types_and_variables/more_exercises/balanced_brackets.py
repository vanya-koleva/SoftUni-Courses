number_of_lines = int(input())
last_printed_bracket = ""
is_balanced = True

for i in range(number_of_lines):
    symbol = input()
    if symbol == "(":
        if last_printed_bracket == "(":
            is_balanced = False
        else:
            last_printed_bracket = symbol

    elif symbol == ")":
        if last_printed_bracket == ")" or last_printed_bracket == "":
            is_balanced = False
        elif last_printed_bracket == "(":
            last_printed_bracket = ""

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
