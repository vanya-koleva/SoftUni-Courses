def eat_cookie(gifts: int, good_kids_visited: int):
    for coordinates in directions.values():
        row, col = santa[0] + coordinates[0], santa[1] + coordinates[1]

        if matrix[row][col].isalpha():
            if matrix[row][col] == "V":
                good_kids_visited += 1
            gifts -= 1
            matrix[row][col] = "-"

        if not gifts:
            break

    return gifts, good_kids_visited


presents = int(input())
n = int(input())
matrix = []
santa = []
nice_kids = 0
nice_kids_visited = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(n):
    matrix.append(input().split())

    if "S" in matrix[i]:
        santa = [i, matrix[i].index("S")]
        matrix[i][santa[1]] = "-"

    nice_kids += matrix[i].count("V")

while presents:
    command = input()

    if command == "Christmas morning":
        break

    r, c = santa[0] + directions[command][0], santa[1] + directions[command][1]

    santa = [r, c]

    if matrix[r][c] == "V":
        presents -= 1
        nice_kids_visited += 1

    elif matrix[r][c] == "C":
        presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)

    matrix[r][c] = "-"

matrix[santa[0]][santa[1]] = "S"

if not presents and nice_kids_visited < nice_kids:
    print("Santa ran out of presents!")

print(*[" ".join(x) for x in matrix], sep="\n")

if nice_kids == nice_kids_visited:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_visited} nice kid/s.")
