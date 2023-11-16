budget = float(input())
season = input()
accommodation = ''
location = ''
price = 0

if budget <= 1000:
    accommodation = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    else:
        location = 'Morocco'
        price = budget * 0.45
elif budget <= 3000:
    accommodation = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.8
    else:
        location = 'Morocco'
        price = budget * 0.6
else:
    accommodation = 'Hotel'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.9
    else:
        location = 'Morocco'
        price = budget * 0.9
print(f'{location} - {accommodation} - {price:.02f}')