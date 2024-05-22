rows, col = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    sublist = [int(x) for x in input().split()]
    matrix.append(sublist)

for j in range(col):
    total_sum = 0
    for i in range(rows):
        total_sum += matrix[i][j]
    print(total_sum)
