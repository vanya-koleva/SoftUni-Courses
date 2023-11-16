budget = int(input())
season = input()
number_of_fishermen = int(input())
rent = 0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
else:
    rent = 2600

if number_of_fishermen <= 6:
    rent *= 0.9
elif number_of_fishermen <= 11:
    rent *= 0.85
else:
    rent *= 0.75

if number_of_fishermen % 2 == 0 and season != 'Autumn':
    rent *= 0.95

difference = abs(rent - budget)
if budget >= rent:
    print(f'Yes! You have {difference:.02f} leva left.')
else:
    print(f'Not enough money! You need {difference:.02f} leva.')