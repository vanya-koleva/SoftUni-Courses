from math import floor, ceil

grape_area = int(input())
grape_per_meter = float(input())
needed_wine = int(input())
number_of_workers = int(input())

total_harvest = grape_area * grape_per_meter
harvest_for_wine = total_harvest * 0.4
total_wine = harvest_for_wine / 2.5
difference = abs(total_wine - needed_wine)
wine_per_worker = difference / number_of_workers

if total_wine >= needed_wine:
    print(f"Good harvest this year! Total wine: {floor(total_wine)} liters.")
    print(f"{ceil(difference)} liters left -> {ceil(wine_per_worker)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(difference)} liters wine needed.")