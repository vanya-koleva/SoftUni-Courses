expression = input()
paren_idx = []

for idx in range(len(expression)):
    if expression[idx] == "(":
        paren_idx.append(idx)
    elif expression[idx] == ")":
        start_idx = paren_idx.pop()
        end_idx = idx + 1
        print(expression[start_idx:end_idx])
