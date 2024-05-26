def valid_index(x: int, y: int) -> bool:
    return 0 <= x < SIZE and 0 <= y < SIZE


def move(direction: str, steps: int) -> list:
    r = player[0] + directions[direction][0] * steps
    c = player[1] + directions[direction][1] * steps

    if valid_index(r, c):
        if matrix[r][c] == ".":
            return [r, c]

    return player


def shoot(direction: str):
    r = player[0] + directions[direction][0]
    c = player[1] + directions[direction][1]

    while valid_index(r, c):
        if matrix[r][c] == "x":
            matrix[r][c] = "."
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


SIZE = 5
matrix = []
player = []
total_targets = 0
targets_hit = 0
targets_hit_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    matrix.append(input().split())

    if "A" in matrix[row]:
        player = [row, matrix[row].index("A")]
        matrix[row][player[1]] = "."

    total_targets += matrix[row].count("x")

for _ in range(int(input())):
    command_info = input().split()

    if "move" in command_info:
        player = move(command_info[1], int(command_info[2]))

    elif "shoot" in command_info:
        target_shot_pos = shoot(command_info[1])

        if target_shot_pos:
            targets_hit_pos.append(target_shot_pos)
            targets_hit += 1

    if targets_hit == total_targets:
        print(f"Training completed! All {total_targets} targets hit.")
        break

else:
    print(f"Training not completed! {total_targets - targets_hit} targets left.")

print(*targets_hit_pos, sep="\n")
