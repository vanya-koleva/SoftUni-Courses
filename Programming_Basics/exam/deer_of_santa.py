from math import floor, ceil

days = int(input())
food = int(input())
first_deer = float(input())
second_deer = float(input())
third_deer = float(input())

food_for_first_deer = days * first_deer
food_for_second_deer = days * second_deer
food_for_third_deer = days * third_deer
total_needed_food = food_for_first_deer + food_for_second_deer + food_for_third_deer
difference = abs(total_needed_food - food)

if total_needed_food <= food:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")