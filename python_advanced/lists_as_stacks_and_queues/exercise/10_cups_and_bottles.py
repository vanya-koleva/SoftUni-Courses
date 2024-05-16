from collections import deque

cups = deque(int(x) for x in input().split())
bottles = deque(int(x) for x in input().split())
wasted_water = 0

while cups and bottles:
    bottle = bottles.pop()
    cup = cups.popleft()

    if bottle >= cup:
        wasted_water += (bottle - cup)
    else:
        cups.appendleft(cup - bottle)

if not cups:
    print("Bottles:", *bottles)
else:
    print("Cups:", *cups)

print(f"Wasted litters of water: {wasted_water}")
