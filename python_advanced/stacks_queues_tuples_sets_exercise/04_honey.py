from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0

mapper = {
    "*": lambda x,y: x * y,
    "/": lambda x,y: x / y if y != 0 else 0,
    "+": lambda x,y: x + y,
    "-": lambda x,y: x - y,
}

while bees and nectar:
    curr_bee = bees.popleft()
    curr_nectar = nectar.pop()

    if curr_nectar >= curr_bee:
        honey += abs(mapper[symbols.popleft()](curr_bee, curr_nectar))
    else:
        bees.appendleft(curr_bee)

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
