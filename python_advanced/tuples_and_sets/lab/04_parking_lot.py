cars = set()

mapper = {
    "IN": lambda x: cars.add(x),
    "OUT": lambda x: cars.remove(x) if x in cars else None
}

for _ in range(int(input())):
    direction, car = input().split(", ")
    mapper[direction](car)

if cars:
    print(*cars, sep="\n")
else:
    print("Parking Lot is Empty")
