budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_for_others = int(input())

if number_of_nights > 7:
    price_per_night *= 0.95
total_sum = number_of_nights * price_per_night
percent_for_others = budget * (percent_for_others / 100)
total_sum += percent_for_others
difference = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")