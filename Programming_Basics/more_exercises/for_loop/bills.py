number_of_months = int(input())
monthly_water = 20
monthly_internet = 15
monthly_others = 0
total_electricity = 0
total_others = 0
total_sum = 0

for i in range(number_of_months):
    monthly_electricity = float(input())
    total_electricity += monthly_electricity
    total_sum += monthly_electricity
    monthly_others = (monthly_electricity + monthly_water + monthly_internet)\
                     + (monthly_electricity + monthly_water + monthly_internet) * 0.2
    total_others += monthly_others
    total_sum += monthly_others
total_water = monthly_water * number_of_months
total_internet = monthly_internet * number_of_months
total_sum += total_water + total_internet
average = total_sum / number_of_months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {average:.2f} lv")