from functools import reduce


def operate(operator, *args):
    operators = {
        "+": lambda x: reduce(lambda a, b: a + b, x),
        "-": lambda x: reduce(lambda a, b: a - b, x),
        "*": lambda x: reduce(lambda a, b: a * b, x),
        "/": lambda x: reduce(lambda a, b: a / b, x),
    }

    return operators[operator](args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
