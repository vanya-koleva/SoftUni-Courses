days = int(input())
hours = int(input())
total_sum = 0

for i in range(1, days + 1):
    price_per_day = 0
    for h in range(1, hours + 1):
        if i % 2 == 0 and h % 2 != 0:
            price_per_hour = 2.5
        elif i % 2 != 0 and h % 2 == 0:
            price_per_hour = 1.25
        else:
            price_per_hour = 1
        price_per_day += price_per_hour
    print(f"Day: {i} - {price_per_day:.2f} leva")
    total_sum += price_per_day

print(f"Total: {total_sum:.2f} leva")

