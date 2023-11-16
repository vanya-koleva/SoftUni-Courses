holiday_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

total_puzzles =number_of_puzzles * 2.6
total_dolls = number_of_dolls * 3
total_bears = number_of_bears * 4.1
total_minions = number_of_minions * 8.2
total_trucks = number_of_trucks * 2
total_sum = total_puzzles + total_dolls + total_bears + total_minions + total_trucks
number_of_toys = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks
if number_of_toys >= 50:
    total_sum *= 0.75
total_sum *= 0.9
difference = abs(total_sum - holiday_price)
if total_sum >= holiday_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
