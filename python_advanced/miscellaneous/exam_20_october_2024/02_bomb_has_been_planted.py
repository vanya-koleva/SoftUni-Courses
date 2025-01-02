def check_boundaries(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def read_matrix_and_position(n, m):
    matrix = []
    position = []
    for i in range(n):
        line = list(input())
        matrix.append(line)
        if "C" in line:
            position = [i, line.index("C")]
    return matrix, position

def print_result_and_matrix(result, matrix):
    print("\n".join(result))
    for row in matrix:
        print("".join(row))

n, m = map(int, input().split(", "))
matrix, position = read_matrix_and_position(n, m)

is_defused = False
has_exploded = False
remaining_time = 16
element = ""

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

while True:
    if remaining_time <= 0:
        has_exploded = True
        break

    command = input()

    if command == "defuse":
        if element != "B":
            remaining_time -= 2
            continue

        remaining_time -= 4
        if remaining_time >= 0:
            is_defused = True
            matrix[position[0]][position[1]] = "D"
        else:
            matrix[position[0]][position[1]] = "X"
            has_exploded = True
        break

    r, c = position[0] + directions[command][0], position[1] + directions[command][1]

    remaining_time -= 1

    if not check_boundaries(r, c, n, m):
        continue

    position = [r, c]
    element = matrix[r][c]

    if element == "T":
        matrix[r][c] = "*"
        break

if has_exploded:
    needed_time = abs(remaining_time)
    result = [
        "Terrorists win!",
        "Bomb was not defused successfully!",
        f"Time needed: {needed_time} second/s."
    ]
elif is_defused:
    result = [
        "Counter-terrorist wins!",
        f"Bomb has been defused: {remaining_time} second/s remaining."
    ]
else:
    result = ["Terrorists win!"]

print_result_and_matrix(result, matrix)
