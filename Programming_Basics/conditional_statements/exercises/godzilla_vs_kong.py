budget = float(input())
number_of_statists = int(input())
clothing_for_one_statist = float(input())

decor = budget * 0.1
total_clothing = number_of_statists * clothing_for_one_statist
if number_of_statists >= 150:
    total_clothing *= 0.9
needed_sum = decor + total_clothing
difference = abs(needed_sum - budget)
if needed_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.02f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.02f} leva left.")