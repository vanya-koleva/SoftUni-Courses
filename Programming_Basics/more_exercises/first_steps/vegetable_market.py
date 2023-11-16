price_vegetables_per_kg = float(input())
price_fruits_per_kg = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())

total_income = (price_vegetables_per_kg * vegetables_kg + price_fruits_per_kg * fruits_kg) / 1.94
print(f"{total_income:.02f}")