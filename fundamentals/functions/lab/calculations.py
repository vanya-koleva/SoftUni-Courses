input_operator = input()
first_number = int(input())
second_number = int(input())


def calculation(operator, num1, num2):
    """Calculates a result depending on the operator"""
    result = None
    if operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = num1 // num2
    elif operator == "add":
        result = num1 + num2
    elif operator == "subtract":
        result = num1 - num2
    return result


print(calculation(input_operator, first_number, second_number))
