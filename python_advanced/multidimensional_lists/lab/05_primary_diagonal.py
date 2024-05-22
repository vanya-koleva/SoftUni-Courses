n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

sum_diagonal = 0
for idx in range(n):
    sum_diagonal += matrix[idx][idx]

print(sum_diagonal)
