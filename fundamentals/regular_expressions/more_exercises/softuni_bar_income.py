import re

pattern = r".*%([A-Z][a-z]+)%.*<(\w+)>.*\|(\d+)\|\D*(\d+(?:\.\d+)?)\$"
total_income = 0

while True:
    line = input()
    if line == "end of shift":
        break

    matches = re.search(pattern, line)
    if matches:
        customer_name, product, count, price = matches.groups()
        total_price = int(count) * float(price)
        print(f"{customer_name}: {product} - {total_price:.2f}")
        total_income += total_price

print(f"Total income: {total_income:.2f}")
