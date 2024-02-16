def multiplication_sign(first_number, second_number, third_number):
    if first_number == 0 or second_number == 0 or third_number == 0:
        return "zero"
    elif sum([first_number < 0, second_number < 0, third_number < 0]) % 2 == 0:
        return "positive"
    else:
        return "negative"


num1, num2, num3 = int(input()), int(input()), int(input())
print(multiplication_sign(num1, num2, num3))
