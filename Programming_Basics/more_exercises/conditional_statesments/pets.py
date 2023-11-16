from math import ceil, floor

days = int(input())
food_given = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day_in_gr = float(input())

needed_dog_food = days * dog_food_per_day
needed_cat_food = days * cat_food_per_day
needed_turtle_food = days * turtle_food_per_day_in_gr / 1000
total_needed_food = needed_dog_food + needed_cat_food + needed_turtle_food
difference = abs(total_needed_food - food_given)

if total_needed_food < food_given:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")