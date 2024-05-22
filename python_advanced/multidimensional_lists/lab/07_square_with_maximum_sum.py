rows, col = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

max_sum = float("-inf")
square = None

for i in range(rows - 1):
    for j in range(col - 1):
        current = matrix[i][j]
        next_el = matrix[i][j + 1]
        below = matrix[i + 1][j]
        diagonal = matrix[i + 1][j + 1]

        sum_square = current + next_el + below + diagonal
        if sum_square > max_sum:
            max_sum = sum_square
            square = [[current, next_el], [below, diagonal]]

if square:
    print(*square[0])
    print(*square[1])

print(max_sum)
