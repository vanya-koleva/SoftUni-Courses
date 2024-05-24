n = int(input())
commands = input().split()

matrix = []
position = []
collected_coal, total_coal = 0, 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

for row in range(n):
    matrix.append(input().split())

    if "s" in matrix[row]:
        position = [row, matrix[row].index("s")]
        matrix[position[0]][position[1]] = "*"

    total_coal += matrix[row].count("c")

for command in commands:
    r, c = position[0] + directions[command][0], position[1] + directions[command][1]

    if not (0 <= r < n and 0 <= c < n):
        continue

    position = [r, c]

    if matrix[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        break

    elif matrix[r][c] == "c":
        collected_coal += 1
        matrix[r][c] = "*"

        if collected_coal == total_coal:
            print(f"You collected all coal! ({r}, {c})")
            break

else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({position[0]}, {position[1]})")
