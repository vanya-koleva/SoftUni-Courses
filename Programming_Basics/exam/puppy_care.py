food_bought = int(input())
food_bought *= 1000
food_eaten = 0

command = input()
while command != "Adopted":
    food_eaten_per_meal = int(command)
    food_eaten += food_eaten_per_meal
    command = input()

difference = abs(food_eaten - food_bought)
if food_bought >= food_eaten:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")