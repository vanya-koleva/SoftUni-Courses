def calculate_the_factorial(some_number):
    result = some_number
    for number in range(1, some_number):
        result *= number
    return result


first_number = int(input())
second_number = int(input())
first_number_factorial = calculate_the_factorial(first_number)
second_number_factorial = calculate_the_factorial(second_number)
final_result = first_number_factorial / second_number_factorial
print(f"{final_result:.2f}")
