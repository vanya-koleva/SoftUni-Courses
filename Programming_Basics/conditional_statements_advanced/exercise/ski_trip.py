days = int(input())
type_of_room = input()
grade = input()
nights = days - 1

if type_of_room == 'room for one person':
    price_per_night = 18
elif type_of_room == 'apartment':
    price_per_night = 25
    if nights < 10:
        price_per_night *= 0.7
    elif nights < 15:
        price_per_night *= 0.65
    else:
        price_per_night *= 0.5
else:
    price_per_night = 35
    if nights < 10:
        price_per_night *= 0.9
    elif nights < 15:
        price_per_night *= 0.85
    else:
        price_per_night *= 0.8

total_price = price_per_night * nights
if grade == 'positive':
    total_price *= 1.25
else:
    total_price *= 0.9
print(f'{total_price:.02f}')