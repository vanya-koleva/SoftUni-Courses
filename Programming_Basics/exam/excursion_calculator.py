number_of_people = int(input())
season = input()

if season == "spring":
    if number_of_people <= 5:
        price = 50
    else:
        price = 48
elif season == "summer":
    if number_of_people <= 5:
        price = 48.5
    else:
        price = 45
elif season == "autumn":
    if number_of_people <= 5:
        price = 60
    else:
        price = 49.5
else:
    if number_of_people <= 5:
        price = 86
    else:
        price = 85

total_sum = number_of_people * price
if season == "summer":
    total_sum *= 0.85
elif season == "winter":
    total_sum *= 1.08

print(f"{total_sum:.2f} leva.")