def valid_index(x: int, y: int) -> bool:
    return 0 <= x < n and 0 <= y < n


n = int(input())
health = 100
matrix = []
position = []
exit_found = False

mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(n):
    line = list(input())
    matrix.append(line)
    if "P" in line:
        position = [i, matrix[i].index("P")]
        matrix[position[0]][position[1]] = "-"

while not exit_found and health > 0:
    direction = input()

    r, c = position[0] + mapper[direction][0], position[1] + mapper[direction][1]

    if not valid_index(r, c):
        continue

    position = [r, c]

    if matrix[r][c] == "X":
        exit_found = True

    elif matrix[r][c] == "M":
        health -= 40
        if health < 0:
            health = 0

    elif matrix[r][c] == "H":
        health = min(100, health + 15)

    matrix[r][c] = "-"

matrix[position[0]][position[1]] = "P"

if exit_found:
    print("Player escaped the maze. Danger passed!")
else:
    print("Player is dead. Maze over!")

print(f"Player's health: {health} units")
[print("".join(r))for r in matrix]
