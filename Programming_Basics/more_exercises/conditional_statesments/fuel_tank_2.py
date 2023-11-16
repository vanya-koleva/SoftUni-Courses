type_of_fuel = input()
amount_of_fuel = float(input())
has_club_card = input()
price_per_litre = 0

if type_of_fuel == "Gasoline":
    price_per_litre = 2.22
    if has_club_card == "Yes":
        price_per_litre -= 0.18
elif type_of_fuel == "Diesel":
    price_per_litre = 2.33
    if has_club_card == "Yes":
        price_per_litre -= 0.12
else:
    price_per_litre = 0.93
    if has_club_card == "Yes":
        price_per_litre -= 0.08

total_price = amount_of_fuel * price_per_litre
if 20 <= amount_of_fuel <= 25:
    total_price *= 0.92
elif amount_of_fuel > 25:
    total_price *= 0.9

print(f"{total_price:.02f} lv.")