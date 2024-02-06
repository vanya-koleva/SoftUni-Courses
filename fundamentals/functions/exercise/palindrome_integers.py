def is_palindrome(some_number:str) -> bool:
    return some_number == some_number[:: - 1]


numbers = input().split(", ")
for number in numbers:
    print(is_palindrome(number))
