from collections import deque
from datetime import datetime, timedelta

robots = {}

for r in input().split(";"):
    name, process_time = r.split("-")
    robots[name] = [int(process_time), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()

    free_robots = []

    for name, value in robots.items():
        current_time = value[1]
        process_time = value[0]

        if value[1] > 0:
            robots[name][1] -= 1

        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue

    name, value = free_robots[0]
    robots[name][1] = value[0]

    print(f"{name} - {product} [{factory_time.strftime('%H:%M:%S')}]")
