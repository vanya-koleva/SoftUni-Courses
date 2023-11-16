nylon_price = 1.50
paint_price = 14.50
paint_thinner_price = 5

needed_nylon = int(input())
needed_paint = int(input())
needed_paint_thinner = int(input())
needed_hours = int(input())

total_nylon = (needed_nylon + 2) * nylon_price
total_paint = (needed_paint + needed_paint * 0.1) * paint_price
total_paint_thinner = needed_paint_thinner * paint_thinner_price
total_materials = total_nylon + total_paint + total_paint_thinner + 0.40
workers = (total_materials * 0.3) * needed_hours
total_sum = total_materials + workers
print (total_sum)
