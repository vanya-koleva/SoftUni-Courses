numbers = input().split()


def rounded(some_list):
    rounded_numbers = [round(float(number)) for number in some_list]
    return rounded_numbers


print(rounded(numbers))
