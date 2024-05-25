n = int(input())
matrix = [list(input()) for _ in range(n)]
removed_knights = 0

pos_nums = (2, 1, -2, -1)
positions = [(x, y) for x in pos_nums for y in pos_nums if abs(x) != abs(y)]

while True:
    most_dangerous_knight = []
    max_attacks = 0

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    r, c = row + pos[0], col + pos[1]
                    if 0 <= r < n and 0 <= c < n:
                        if matrix[r][c] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    most_dangerous_knight = [row, col]

    if most_dangerous_knight:
        matrix[most_dangerous_knight[0]][most_dangerous_knight[1]] = 0
        removed_knights += 1
    else:
        break

print(removed_knights)
