bakery_stock = input().split()
searched_products = input().split()
bakery_stock_table = {}

for i in range(0, len(bakery_stock), 2):
    key = bakery_stock[i]
    value = int(bakery_stock[i + 1])
    bakery_stock_table[key] = value

for product in searched_products:
    if product in bakery_stock_table:
        print(f"We have {bakery_stock_table[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
