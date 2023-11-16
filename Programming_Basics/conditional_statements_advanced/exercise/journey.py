budget = float(input())
season = input()
destination = ''
sum_spent = 0
type_of_holiday = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        sum_spent = budget * 0.3
    else:
        sum_spent = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        sum_spent = budget * 0.4
    else:
        sum_spent = budget * 0.8
else:
    destination = 'Europe'
    sum_spent = budget * 0.9

if season == 'summer' and destination != 'Europe':
    type_of_holiday = 'Camp'
else:
    type_of_holiday = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{type_of_holiday} - {sum_spent:.02f}')