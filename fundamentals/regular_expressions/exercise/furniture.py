import re

pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
bought_furniture = []
total_price = 0

while True:
    line = input()
    if line == "Purchase":
        break

    matches = re.search(pattern, line)
    if matches:
        furniture_name, price, quantity = matches.groups()
        bought_furniture.append(furniture_name)
        total_price += float(price) * int(quantity)

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")
