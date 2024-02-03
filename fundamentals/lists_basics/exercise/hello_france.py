items = input().split("|")
budget = float(input())
new_prices = []
sum_of_bought_items = 0
sum_of_new_prices = 0
maximum_price_of_clothes = 50.00
maximum_price_of_shoes = 35.00
maximum_price_of_accessories = 20.50

for item in items:
    item = item.split("->")
    price = float(item[1])
    item = item[0]

    if (item == "Clothes" and price > maximum_price_of_clothes)\
            or (item == "Shoes" and price > maximum_price_of_shoes)\
            or (item == "Accessories" and price > maximum_price_of_accessories):
        continue

    if budget - price < 0:
        continue

    budget -= price
    sum_of_bought_items += price
    price = float(price) * 1.4
    sum_of_new_prices += price
    new_prices.append(f'{price:.2f}')

profit = sum_of_new_prices - sum_of_bought_items

print(" ".join(new_prices))
print(f"Profit: {profit:.2f}")

if budget + sum_of_new_prices >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
