rows, col = [int(x) for x in input().split(", ")]
matrix = []
total_sum = 0

for i in range(rows):
    sublist = [int(x) for x in input().split(", ")]
    total_sum += sum(sublist)
    matrix.append(sublist)

print(total_sum)
print(matrix)
