budget = float(input())
category = input()
number_of_people = int(input())

if 1 <= number_of_people <= 4:
    budget *= 0.25
elif number_of_people <= 9:
    budget *= 0.4
elif number_of_people <= 24:
    budget *= 0.5
elif number_of_people <= 49:
    budget *= 0.6
else:
    budget *= 0.75

if category == 'VIP':
    ticket_price = 499.99
else:
    ticket_price = 249.99

total_price = number_of_people * ticket_price
difference = abs(budget - total_price)
if total_price <= budget:
    print(f"Yes! You have {difference:.02f} leva left.")
else:
    print(f"Not enough money! You need {difference:.02f} leva.")