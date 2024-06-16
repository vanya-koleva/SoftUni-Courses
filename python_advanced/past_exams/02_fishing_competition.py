def handle_boundaries(pos, size):
    for i in range(2):
        if pos[i] >= size:
            pos[i] = 0
        elif pos[i] < 0:
            pos[i] = size - 1
    return pos


n = int(input())
position = []
matrix = []
fish = 0
quota = 20
whirlpool = False

for i in range(n):
    line = list(input())
    matrix.append(line)
    if "S" in line:
        position = [i, matrix[i].index("S")]
        matrix[position[0]][position[1]] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    if command == "collect the nets":
        break

    r, c = position[0] + directions[command][0], position[1] + directions[command][1]
    position = handle_boundaries([r, c], n)

    element = matrix[position[0]][position[1]]
    matrix[position[0]][position[1]] = "-"

    if element == "W":
        whirlpool = True
        fish = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{position[0]},{position[1]}]")
        break

    elif element.isdigit():
        fish += int(element)

matrix[position[0]][position[1]] = "S"

if fish >= quota:
    print("Success! You managed to reach the quota!")
elif not whirlpool:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {quota - fish} tons of fish more.")

if fish > 0:
    print(f"Amount of fish caught: {fish} tons.")

if not whirlpool:
    [print(''.join(r)) for r in matrix]
