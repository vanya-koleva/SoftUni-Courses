# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ",
# and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted as a positive number
def positive_numbers(list_of_numbers):
    return ", ".join([str(x) for x in list_of_numbers if x >= 0])


def negative_numbers(list_of_numbers):
    return ", ".join([str(x) for x in list_of_numbers if x < 0])


def even_numbers(list_of_numbers):
    return ", ".join([str(x) for x in list_of_numbers if x % 2 == 0])


def odd_numbers(list_of_numbers):
    return ", ".join([str(x) for x in list_of_numbers if x % 2 != 0])


numbers = [int(x) for x in input().split(", ")]
print(f"Positive: {positive_numbers(numbers)}")
print(f"Negative: {negative_numbers(numbers)}")
print(f"Even: {even_numbers(numbers)}")
print(f"Odd: {odd_numbers(numbers)}")
