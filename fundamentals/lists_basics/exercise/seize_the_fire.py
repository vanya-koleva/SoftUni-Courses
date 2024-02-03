cells = input().split("#")
water = int(input())
high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range(1, 50 + 1)
effort = 0
put_out_cells = []

for cell in cells:
    type_of_fire, value_of_cell = cell.split(" = ")
    value_of_cell = int(value_of_cell)
    if (type_of_fire == "High" and value_of_cell in high) or \
            (type_of_fire == "Medium" and value_of_cell in medium) or \
            (type_of_fire == "Low" and value_of_cell in low):
        if water < value_of_cell:
            continue
        put_out_cells.append(value_of_cell)
        water -= value_of_cell
        effort += value_of_cell * 0.25
total_fire = sum(put_out_cells)

print("Cells:")
for cell in put_out_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
