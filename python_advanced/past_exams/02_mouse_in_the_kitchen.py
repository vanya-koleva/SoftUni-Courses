def valid_index(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


rows, cols = [int(x) for x in input().split(",")]
matrix = []
position = []
pieces_of_cheese = 0

for i in range(rows):
    line = list(input())
    matrix.append(line)
    if "M" in line:
        position = [i, matrix[i].index("M")]
        matrix[position[0]][position[1]] = "*"
    pieces_of_cheese += line.count("C")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    if command == "danger":
        if pieces_of_cheese:
            print("Mouse will come back later!")
        break

    r, c = position[0] + directions[command][0], position[1] + directions[command][1]
    if not valid_index(r, c, rows, cols):
        print("No more cheese for tonight!")
        break

    element = matrix[r][c]

    if element == "@":
        continue

    position = [r, c]
    matrix[r][c] = "*"

    if element == "C":
        pieces_of_cheese -= 1
        if not pieces_of_cheese:
            position = [r, c]
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif element == "T":
        print("Mouse is trapped!")
        break

matrix[position[0]][position[1]] = "M"
[print("".join(r)) for r in matrix]
