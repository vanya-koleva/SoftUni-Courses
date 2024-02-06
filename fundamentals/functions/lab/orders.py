input_product = input()
input_quantity = int(input())
coffee_price = 1.5
water_price = 1.0
coke_price = 1.4
snacks_price = 2.0


def total_price(product, quantity):
    if product == "coffee":
        price = quantity * coffee_price
    elif product == "water":
        price = quantity * water_price
    elif product == "coke":
        price = quantity * coke_price
    elif product == "snacks":
        price = quantity * snacks_price

    return f"{price:.2f}"


print(total_price(input_product, input_quantity))
