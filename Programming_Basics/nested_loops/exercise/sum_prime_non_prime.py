command = input()
prime_sum = 0
non_prime_sum = 0

while command != "stop":
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
        command = input()
        continue
    current_number_is_prime = True
    for number in range(2, current_number):
        if current_number % number == 0:
            current_number_is_prime = False
            break
    if current_number_is_prime:
        prime_sum += current_number
    else:
        non_prime_sum += current_number
    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")