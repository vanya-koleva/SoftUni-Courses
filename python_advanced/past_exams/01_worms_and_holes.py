from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())
number_of_worms = len(worms)
matches = 0

while worms and holes:
    worm = worms.pop()
    if worm <= 0:
        continue

    hole = holes.popleft()

    if worm == hole:
        matches += 1
        continue

    worm -= 3
    worms.append(worm)

print(f"Matches: {matches}" if matches else "There are no matches.")

if number_of_worms == matches:
    print("Every worm found a suitable hole!")
else:
    print(f"Worms left: {', '.join(str(x) for x in worms)}" if worms else "Worms left: none")

print(f"Holes left: {', '.join(str(x) for x in holes)}" if holes else "Holes left: none")
