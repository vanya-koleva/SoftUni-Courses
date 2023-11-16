needed_sum = int(input())
total_payments_with_cash = 0
total_payments_with_card = 0
total_payments_counter = 1
card_payments_counter = 0
cash_payments_counter = 0
needed_sum_is_collected = False

command = input()
while command != 'End':
    current_payment = int(command)
    if total_payments_counter % 2 == 0:
        if current_payment < 10:
            print("Error in transaction!")
        else:
            total_payments_with_card += current_payment
            card_payments_counter += 1
            print("Product sold!")
    else:
        if current_payment > 100:
            print("Error in transaction!")
        else:
            total_payments_with_cash += current_payment
            cash_payments_counter += 1
            print("Product sold!")
    if total_payments_with_card + total_payments_with_cash >= needed_sum:
        needed_sum_is_collected = True
        break
    total_payments_counter += 1
    command = input()

if needed_sum_is_collected:
    average_cash = total_payments_with_cash / cash_payments_counter
    average_card = total_payments_with_card / card_payments_counter
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")
else:
    print("Failed to collect required money for charity.")
