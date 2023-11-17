remaining_budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price_per_litre = flour_price * 1.25
milk_price_per_loaf = milk_price_per_litre / 4
price_per_loaf = flour_price + eggs_price + milk_price_per_loaf
number_of_loaves = 0
number_of_colored_eggs = 0

while remaining_budget > price_per_loaf:
    remaining_budget -= price_per_loaf
    number_of_loaves += 1
    number_of_colored_eggs += 3
    if number_of_loaves % 3 == 0:
        number_of_colored_eggs -= number_of_loaves - 2

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {number_of_colored_eggs} eggs and {remaining_budget:.2f}BGN left.")
