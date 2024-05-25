rows, cols = [int(x) for x in input().split()]
matrix = []
player_r, player_c = 0, 0
bunnies = set()
won = False
dead = False

directions = {
    "U": lambda r, c: (r - 1, c),
    "D": lambda r, c: (r + 1, c),
    "R": lambda r, c: (r, c + 1),
    "L": lambda r, c: (r, c - 1),
}

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == "P":
            player_r, player_c = row, col
        elif matrix[row][col] == "B":
            bunnies.add((row, col))

commands = list(input())


def valid_index(index_row, index_column):
    return 0 <= index_row < rows and 0 <= index_column < cols


def spread_bunnies(mat, bunnies_set):
    new_bunnies = set()

    for bunny in bunnies_set:
        b_row, b_col = bunny
        for d in ["U", "D", "L", "R"]:
            new_b_r, new_b_c = directions[d](b_row, b_col)
            if valid_index(new_b_r, new_b_c):
                mat[new_b_r][new_b_c] = "B"
                new_bunnies.add((new_b_r, new_b_c))

    return mat, bunnies_set.union(new_bunnies)


for command in commands:
    new_p_r, new_p_c = directions[command](player_r, player_c)
    matrix, bunnies = spread_bunnies(matrix, bunnies)
    matrix[player_r][player_c] = "." if (player_r, player_c) not in bunnies else "B"

    if not valid_index(new_p_r, new_p_c):
        won = True
        break

    player_r, player_c = new_p_r, new_p_c

    if matrix[new_p_r][new_p_c] == "B":
        dead = True
        break

[print(*row, sep="") for row in matrix]

if won:
    print(f"won: {player_r} {player_c}")
else:
    print(f"dead: {player_r} {player_c}")
