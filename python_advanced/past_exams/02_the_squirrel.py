from collections import deque


def valid_index(x: int, y: int) -> bool:
    return 0 <= x < n and 0 <= y < n


n = int(input())
commands = deque(input().split(", "))
matrix = []
position = []

for i in range(n):
    line = list(input())
    matrix.append(line)
    if "s" in line:
        position = [i, matrix[i].index("s")]
        matrix[position[0]][position[1]] = "*"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

hazelnuts = 0

while commands:
    command = commands.popleft()
    r, c = position[0] + directions[command][0], position[1] + directions[command][1]

    if not valid_index(r, c):
        print("The squirrel is out of the field.")
        break

    position = [r, c]
    element = matrix[r][c]

    if element == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    elif element == "h":
        hazelnuts += 1
        matrix[r][c] = "*"
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
