number_of_junior_racers = int(input())
number_of_senior_racers = int(input())
type_of_track = input()
price_for_juniors = 0
price_for_seniors = 0

if type_of_track == 'trail':
    price_for_juniors = 5.5
    price_for_seniors = 7
elif type_of_track == "cross-country":
    price_for_juniors = 8
    price_for_seniors = 9.5
elif type_of_track == "downhill":
    price_for_juniors = 12.25
    price_for_seniors = 13.75
else:
    price_for_juniors = 20
    price_for_seniors = 21.5

total_price = price_for_juniors * number_of_junior_racers + price_for_seniors * number_of_senior_racers
if number_of_junior_racers + number_of_senior_racers >= 50 and type_of_track == "cross-country":
    total_price *= 0.75
total_price *= 0.95

print(f'{total_price:.02f}')