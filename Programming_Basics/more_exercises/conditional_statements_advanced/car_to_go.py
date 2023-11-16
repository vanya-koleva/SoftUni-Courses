budget = float(input())
season = input()
class_of_car = ''
type_of_car = ''
price = 0
if budget <= 100:
    class_of_car = 'Economy class'
    if season == 'Summer':
        type_of_car = 'Cabrio'
        price = budget * 0.35
    else:
        type_of_car = 'Jeep'
        price = budget * 0.65
elif budget <= 500:
    class_of_car = 'Compact class'
    if season == 'Summer':
        type_of_car = 'Cabrio'
        price = budget * 0.45
    else:
        type_of_car = 'Jeep'
        price = budget * 0.8
else:
    class_of_car = 'Luxury class'
    type_of_car = 'Jeep'
    price = budget * 0.9

print(f"{class_of_car}")
print(f"{type_of_car} - {price:.02f}")