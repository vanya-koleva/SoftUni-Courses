from math import ceil

days = int(input())
km_run = float(input())
goal = 1000
total_km = km_run

for _ in range(days):
    percentage = int(input())
    percentage /= 100
    km_run = km_run + (km_run * percentage)
    total_km += km_run

difference = abs(total_km - goal)
if total_km >= goal:
    print(f"You've done a great job running {ceil(difference)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(difference)} more kilometers")