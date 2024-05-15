from collections import deque

parentheses = deque(input())
opening_parentheses = deque()
opening = "({["
pairs = "(){}[]"

while parentheses:
    current = parentheses.popleft()

    if current in opening:
        opening_parentheses.append(current)

    elif not opening_parentheses:
        print("NO")
        break

    else:
        if opening_parentheses.pop() + current not in pairs:
            print("NO")
            break

else:
    print("YES")
