fats_percentage = int(input())
proteins_percentage = int(input())
carbohydrates_percentage = int(input())
total_calories = int(input())
water_percentage = int(input())

total_fats = (total_calories * fats_percentage / 100) / 9
total_proteins = (total_calories * proteins_percentage / 100) / 4
total_carbohydrates = (total_calories * carbohydrates_percentage / 100) / 4
food_weight = total_fats + total_proteins + total_carbohydrates
total_calories_per_gram = total_calories / food_weight
calories_per_gram = total_calories_per_gram * (1 -water_percentage / 100)
print(f"{calories_per_gram:.4f}")
