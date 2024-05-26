n = int(input())
matrix = []
bunny = []
best_direction = ""
best_path = []
most_eggs = float("-inf")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    matrix.append(input().split())

    if "B" in matrix[row]:
        bunny = [row, matrix[row].index("B")]

for direction, position in directions.items():
    eggs = 0
    path = []
    row, col = bunny[0] + position[0], bunny[1] + position[1]

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "X":
            break

        eggs += int(matrix[row][col])
        path.append([row, col])

        row += position[0]
        col += position[1]

    if eggs >= most_eggs:
        most_eggs = eggs
        best_path = path
        best_direction = direction

print(best_direction)
print(*best_path, sep="\n")
print(most_eggs)
