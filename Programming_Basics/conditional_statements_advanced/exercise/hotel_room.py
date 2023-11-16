month = input()
number_of_nights = int(input())
price = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if 7 < number_of_nights <= 14:
        studio_price *= 0.95
    elif number_of_nights > 14:
        studio_price *= 0.7
elif month == 'June' or month == 'September':
    studio_price = 75.2
    apartment_price = 68.7
    if number_of_nights > 14:
        studio_price *= 0.8
else:
    studio_price = 76
    apartment_price = 77

if number_of_nights > 14:
    apartment_price *= 0.9

studio_total_price = studio_price * number_of_nights
apartment_total_price = apartment_price * number_of_nights

print(f'Apartment: {apartment_total_price:.02f} lv.')
print(f'Studio: {studio_total_price:.02f} lv.')
