def check_boundaries(x, y, r_number, c_number) -> bool:
    return 0 <= x < r_number and 0 <= y < c_number


rows, cols = (int(x) for x in input().split())
matrix = []
starting_position = []

for i in range(rows):
    line = list(input())
    matrix.append(line)
    if "B" in line:
        starting_position = [i, matrix[i].index("B")]
        matrix[starting_position[0]][starting_position[1]] = "."

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

position = starting_position

while True:
    command = input()
    r, c = position[0] + directions[command][0], position[1] + directions[command][1]

    if not check_boundaries(r, c, rows, cols):
        matrix[starting_position[0]][starting_position[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

    if matrix[r][c] == "*":
        continue

    position = [r, c]
    element = matrix[r][c]
    matrix[r][c] = "."

    if element == "P":
        matrix[r][c] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif element == "A":
        matrix[r][c] = "P"
        matrix[starting_position[0]][starting_position[1]] = "B"
        print("Pizza is delivered on time! Next order...")
        break

[print("".join(x)) for x in matrix]
