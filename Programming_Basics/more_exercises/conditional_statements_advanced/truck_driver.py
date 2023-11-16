season = input()
km_per_month = float(input())
money_per_km = 0

if km_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        money_per_km = 0.75
    elif season == 'Summer':
        money_per_km = 0.9
    else:
        money_per_km = 1.05
elif km_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        money_per_km = 0.95
    elif season == 'Summer':
        money_per_km = 1.1
    else:
        money_per_km = 1.25
elif km_per_month <= 20000:
    money_per_km = 1.45

total_money = money_per_km * km_per_month * 4
total_money *= 0.9

print(f'{total_money:.02f}')