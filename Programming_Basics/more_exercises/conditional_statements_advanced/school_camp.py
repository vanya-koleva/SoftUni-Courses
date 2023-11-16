season = input()
type_of_group = input()
number_of_students = int(input())
number_of_nights = int(input())
price_per_night = 0
sport = ''

if type_of_group == 'boys' or type_of_group == 'girls':
    if season == 'Winter':
        price_per_night = 9.6
        if type_of_group == 'boys':
            sport = 'Judo'
        else:
            sport = "Gymnastics"
    elif season == 'Spring':
        price_per_night = 7.2
        if type_of_group == 'boys':
            sport = 'Tennis'
        else:
            sport = "Athletics"
    else:
        price_per_night = 15
        if type_of_group == 'boys':
            sport = 'Football'
        else:
            sport = "Volleyball"
else:
    if season == 'Winter':
        price_per_night = 10
        sport = 'Ski'
    elif season == 'Spring':
        price_per_night = 9.5
        sport = 'Cycling'
    else:
        price_per_night = 20
        sport = 'Swimming'

total_price = price_per_night * number_of_nights * number_of_students
if number_of_students >= 50:
    total_price *= 0.5
elif 50 > number_of_students >= 20:
    total_price *= 0.85
elif 20 > number_of_students >= 10:
    total_price *= 0.95

print(f'{sport} {total_price:.02f} lv.')
