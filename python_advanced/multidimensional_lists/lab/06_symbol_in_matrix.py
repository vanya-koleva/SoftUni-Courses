n = int(input())
matrix = [[x for x in list(input())] for _ in range(n)]
symbol = input()

position = None

for i in range(n):
    if position:
        break

    for j in range(n):
        if matrix[i][j] == symbol:
            position = (i, j)
            break

if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")
