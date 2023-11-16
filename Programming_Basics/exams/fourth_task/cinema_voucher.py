money_left = int(input())
number_of_tickets_bought = 0
number_of_other_purchases = 0
command = input()

while command != "End":
    if len(command) > 8:
        price = ord(command[0]) + ord(command[1])
        money_left -= price
        if money_left < 0:
            break
        number_of_tickets_bought += 1
    else:
        price = ord(command[0])
        money_left -= price
        if money_left < 0:
            break
        number_of_other_purchases += 1
    command = input()

print(number_of_tickets_bought)
print(number_of_other_purchases)