n = int(input())
matrix = []
enemies = 4
position = []
armor = 300

for i in range(n):
    line = list(input())
    matrix.append(line)
    if "J" in line:
        position = [i, line.index("J")]
        matrix[i][position[1]] = "-"


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    r, c = [position[0] + directions[command][0], position[1] + directions[command][1]]
    position = [r, c]

    element = matrix[r][c]
    matrix[r][c] = "-"

    if element == "E":
        enemies -= 1
        if not enemies:
            print("Mission accomplished, you neutralized the aerial threat!")
            break

        armor -= 100
        if not armor:
            print(f"Mission failed, your jetfighter was shot down! "
                  f"Last coordinates [{r}, {c}]!")
            break

    elif element == "R":
        armor = 300

matrix[r][c] = "J"
[print("".join(r)) for r in matrix]
