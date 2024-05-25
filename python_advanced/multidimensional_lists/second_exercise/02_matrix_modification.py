n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input().split()
    if "END" in command:
        break

    command_type, x, y, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= x < n and 0 <= y < n):
        print("Invalid coordinates")

    elif "Add" in command:
        matrix[x][y] += value

    elif "Subtract" in command:
        matrix[x][y] -= value

[print(*row) for row in matrix]
