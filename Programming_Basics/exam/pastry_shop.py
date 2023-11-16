pastry_type = input()
number_of_pastries = int(input())
day = int(input())

if pastry_type == "Cake":
    if day <= 15:
        price = 24
    else:
        price = 28.7
elif pastry_type == "Souffle":
    if day <= 15:
        price = 6.66
    else:
        price = 9.8
elif pastry_type == "Baklava":
    if day <= 15:
        price = 12.6
    else:
        price = 16.98

total_price = price * number_of_pastries

if day <= 22:
    if 100 <= total_price <= 200:
        total_price *= 0.85
    elif total_price > 200:
        total_price *= 0.75

if day <= 15:
    total_price *= 0.9

print(f"{total_price:.2f}")
