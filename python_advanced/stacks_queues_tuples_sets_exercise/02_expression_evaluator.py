from collections import deque
from functools import reduce

expression = deque(input().split())
numbers = deque()

mapper = {
    "*": lambda x: reduce(lambda a, b: a * b, numbers),
    "/": lambda x: reduce(lambda a, b: a / b, numbers),
    "+": lambda x: reduce(lambda a, b: a + b, numbers),
    "-": lambda x: reduce(lambda a, b: a - b, numbers),
}

for _ in range(len(expression)):
    symbol = expression.popleft()

    if symbol in "*/+-":
        calculation = int(mapper[symbol](numbers))
        numbers.clear()
        numbers.append(calculation)

    else:
        numbers.append(int(symbol))

print(numbers[0])
