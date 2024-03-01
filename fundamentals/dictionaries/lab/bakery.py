bakery_stock = input().split()
bakery_stock_table = {}

for i in range(0, len(bakery_stock), 2):
    key = bakery_stock[i]
    value = int(bakery_stock[i + 1])
    bakery_stock_table[key] = value

print(bakery_stock_table)
