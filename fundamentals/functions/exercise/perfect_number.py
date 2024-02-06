def is_perfect(some_number):
    sum_of_proper_divisors = 0
    for current_number in range(1, some_number):
        if some_number % current_number == 0:
            sum_of_proper_divisors += current_number
    return sum_of_proper_divisors == some_number


number = int(input())
if is_perfect(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
